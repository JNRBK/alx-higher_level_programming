#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance
ARGS:
    id - class attribute that represents a column
    name - class attribute that represents a column
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)


Base.metadata.create_all(engine)
