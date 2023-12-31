#!/usr/bin/python3
""" Moudule contains a script that that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * \
                    FROM states \
                    WHERE BINARY name = '{}'".format(state))

    rows = cursor.fetchall()
    [print(row) for row in rows]

    db.close()
