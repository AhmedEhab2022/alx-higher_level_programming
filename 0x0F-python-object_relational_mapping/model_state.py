#!/usr/bin/python3
"""Module contain the class definition of a State and an
instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """
    State represent states table
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)

    name = Column(String(length=128), nullable=False)
