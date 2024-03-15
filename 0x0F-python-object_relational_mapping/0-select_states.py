#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
ARGS:
    username: name of user in mysql
    password: password used in mysql
    database_name: name of the DB
USAGE:
    ./0-select_states.py root root hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
