#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
ARGS:
    username - mysql username
    passwd - mysql password
    db - database name
    state name - name of state in table to list all cities of
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT GROUP_CONCAT(cities.name) FROM states \
                JOIN cities ON states.id = cities.state_id \
                WHERE states.name = %s", (argv[4],))

    rows = cur.fetchone()

    for row in rows:
        print(row)

    cur.close()
    db.close()
