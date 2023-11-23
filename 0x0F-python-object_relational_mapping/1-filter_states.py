#!/usr/bin/python3
""" Moudule contains a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    db.close()
