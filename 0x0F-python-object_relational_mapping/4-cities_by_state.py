#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
ARGS:
    mysql username, mysql password, database name
USAGE:
    ./file-name.py user passwd db
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
