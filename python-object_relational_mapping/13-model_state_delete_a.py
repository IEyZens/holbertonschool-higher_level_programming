#!/usr/bin/python3
"""
Script that deletes all State objects containing the letter 'a' from a
MySQL database using SQLAlchemy.

Usage:
    ./13-model_state_delete_a.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to the MySQL database using SQLAlchemy
    - Finds all State objects with a name containing the letter 'a'
    - Deletes those State objects from the database

Note:
    The script should not be executed when imported.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name.contains('a'))
        .order_by(State.id)
        .all()
    )

    for s in states:
        session.delete(s)
    session.commit()

    session.close()
