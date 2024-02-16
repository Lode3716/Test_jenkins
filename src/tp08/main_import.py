"""
   
 auth : l.devigne

"""
import csv
import sqlite3


def main():
    with sqlite3.connect("users_db.db") as con:
        cur = con.cursor()

        with open('MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sql = f"""
                    INSERT INTO user_tbl(first_name,last_name,email,gender,ip_address) VALUES (?,?,?,?,?)
                """
                values = [row['first_name'], row['last_name'], row['email'], row['gender'], row['ip_address']]

                cur.execute(sql, values)

    con.close()

    print(row)


if __name__ == '__main__':
    main()
