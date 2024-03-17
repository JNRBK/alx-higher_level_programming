#!/usr/bin/python3
"""
prints all City objects from the database

ARGS:
    ARGV 1 - mysql username
    ARGV 2 - mysql password
    ARGV 3 - database name

USAGE:
    ./file user passwd db_name
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    state_city = (session.query(State.name, City.id, City.name)
                  .join(City, State.id == City.state_id)
                  .order_by(City.id).all())

    for State.name, City.id, City.name in state_city:
        print('{}: ({}) {}'.format(State.name, City.id, City.name))

    session.close()
