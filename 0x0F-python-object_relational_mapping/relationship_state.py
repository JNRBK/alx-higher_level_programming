#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance
ARGS:
    id - class attribute that represents a column
    name - class attribute that represents a column
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states"""
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref='state')
