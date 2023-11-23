#!/usr/bin/python3
""" Moudule contains a script that lists all states from the
database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    sql_query = "SELECT cities.id, cities.name, states.name \
                  FROM states \
                  INNER JOIN cities ON cities.state_id = states.id \
                  ORDER BY cities.id"

    cursor = db.cursor()
    cursor.execute(sql_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
