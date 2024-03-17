#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the database
ARGS:
    ARGV 1 - mysql username
    ARGV 2 - mysql password
    ARGV 3 - database name
USAGE:
    ./file user passwd db_name
"""

from venv import create
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

    a_del = session.query(State).filter(State.name.like("%a%")).all()
    for values in a_del:
        session.delete(values)

    session.commit()
