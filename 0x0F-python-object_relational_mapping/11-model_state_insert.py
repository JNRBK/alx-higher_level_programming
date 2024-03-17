#!/usr/bin/python3
"""
lists all State objects that contain the letter a

ARGS:
    mysql username - mysql server username
    mysql password - mysql password
    database name - name of mysql database
"""
from ast import arg
from audioop import add
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    add_state = State(name='Louisiana')

    session.add(add_state)

    session.commit()

    print('{}'.format(add_state.id))

    session.close()
