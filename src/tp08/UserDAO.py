"""
   
 auth : l.devigne

"""
import sqlite3

from tp07.Singleton import Singleton
from tp08.User import User


class UserDao(metaclass=Singleton):

    def __init__(self, db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    def __del__(self):
        if self.__con:
            self.__con.close()

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, *exc_type):
        print("Exit")
        self.__con.close()
        self.__con = None
        return False

    def findAll(self):
        users = []

        sql = "SELECT * FROM user_tbl"

        cur = self.__con.cursor()

        res = cur.execute(sql)

        for user in res.fetchall():
            u = User(*user)
            # users.append(u)
            # return users
            yield u  # permet de faire une itérateur, optimise la remontée de données en la chargeant à chaque boucle , meilleur pratique en DAO

    def findById(self, id_user: int) -> User:
        sql = "SELECT * FROM user_tbl where id = ?"
        cur = self.__con.cursor()
        res = cur.execute(sql, (id_user,))
        u = res.fetchone()
        return User(*u)
