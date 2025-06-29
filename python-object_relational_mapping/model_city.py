#!/usr/bin/python3
"""
Module defining the City class mapped to the cities table in the database.

This module uses SQLAlchemy to define a City class that links to the MySQL
table 'cities'. Each City has an id, a name, and a foreign key state_id
linking it to a state.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    City class for storing city records in a database.

    Attributes:
        id (int): Unique ID for the city (primary key).
        name (str): Name of the city (max 128 characters, not null).
        state_id (int): Foreign key referencing states.id (not null).
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
