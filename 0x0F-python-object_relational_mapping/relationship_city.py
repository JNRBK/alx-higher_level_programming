#!/usr/bin/python3

#!/usr/bin/python3
"""
Python file model_city.py that contains the class definition of a City
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Class City Inherits from Base
        That links to MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
