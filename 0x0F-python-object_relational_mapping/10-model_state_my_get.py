#!/usr/bin/python3
"""
lists all State objects that contain the letter a

ARGS:
    mysql username - mysql server username
    mysql password - mysql password
    database name - name of mysql database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    state = (session.query(State).filter(State.name == argv[4])
             .order_by(State.id).first())

    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')

    session.close()
