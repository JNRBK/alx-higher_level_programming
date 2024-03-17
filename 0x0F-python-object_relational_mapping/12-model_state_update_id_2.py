#!/usr/bin/python3
"""
changes the name of a State object from the database
ARGS:
    mysql username - mysql server username
    mysql password - mysql password
    database name - name of mysql database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'

    session.commit()
