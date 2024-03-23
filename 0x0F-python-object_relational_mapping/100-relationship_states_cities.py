#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”

ARGS:
    ARGV0 - ./filename
    ARGV1 - username
    ARGV2 - password
    ARGV3 - database name
"""
from venv import create
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine)

    addS = State('California')
    addC = City('San Francisco')

    addS.cities.append(addC)
    session.add(addS)

    session.commit()
