#!/usr/bin/python3
""" Moudule contains a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

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
                    WHERE name = %s", (state,))

    rows = cursor.fetchall()
    [print(row) for row in rows]

    db.close()
