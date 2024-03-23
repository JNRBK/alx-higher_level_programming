#!/usr/bin/python3
"""
Python file model_city.py that contains the class definition of a City
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """Class City Inherits from Base
        That links to MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
