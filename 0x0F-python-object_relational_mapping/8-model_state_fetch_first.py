#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa

ARGS:
    mysql username - mysql server username
    mysql password - mysql password
    database name - name of mysql database
"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    session = Session()

    states = session.query(State).order_by(State.id)

    frst = states.first()

    if frst:
        print('{}: {}'.format(frst.id, frst.name))
    else:
        print('Nothing')
    session.close()
