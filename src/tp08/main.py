"""
   
 auth : l.devigne

"""
from tp08.UserDAO import UserDao


def filtre_male(gen):
    for u in gen:
        if u.gender == "Male":
            yield u


def main():
    with UserDao("users_db.db") as dao:
        dao.findAll()


# dao = UserDao("users_db.db")
#
# users = dao.findAll()
#
# iterateur = next(users)
# print(iterateur)
# iterateur = next(users)
# print(iterateur)
#
# print(dao.findById(573))
#
# for i in filtre_male(users):
#     print(i)
# for user in users:
#     print(user)


if __name__ == '__main__':
    main()
