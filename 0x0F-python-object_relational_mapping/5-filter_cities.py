#!/usr/bin/python3
""" Moudule contains a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    sql_query = "SELECT name FROM cities \
                 WHERE state_id IN (SELECT id FROM states WHERE name = %s) \
                 ORDER BY id"

    cursor = db.cursor()
    cursor.execute(sql_query, (state,))
    rows = cursor.fetchall()
    i = 0
    for row in rows:
        print(row[0], end='')
        if i < len(rows) - 1:
            print(', ', end='')

        i += 1

    print('')
    db.close()
