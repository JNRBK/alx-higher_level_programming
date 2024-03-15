#!/usr/bin/python3
"""
This script connects to a MySQL database and filters
the states table based on a given name.

Args:
    user: The username for the MySQL database.
    passwd: The password for the MySQL database.
    db: The name of the MySQL database.
    do: The name to filter the states table by.

Returns:
    None
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    cur = db.cursor()
    do = argv[4]

    cur.execute('SELECT * FROM states WHERE name = %s ORDER BY id ASC;', (do,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
