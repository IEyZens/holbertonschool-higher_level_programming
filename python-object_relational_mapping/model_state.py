#!/usr/bin/python3
"""
Defines a State class for use with SQLAlchemy ORM.

This class maps to the 'states' table in the MySQL database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents a row in the 'states' table.

    Attributes:
        id (int): The state's unique ID, primary key, auto-incremented.
        name (str): The name of the state, non-nullable, max length 128.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
