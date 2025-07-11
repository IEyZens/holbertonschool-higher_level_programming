#!/usr/bin/python3
"""
Script that lists all State objects from a MySQL database using SQLAlchemy.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to the database using SQLAlchemy
    - Retrieves all entries from the 'states' table
    - Prints the id and name of each State in the format: "<id>: <name>"

Example:
    ./7-model_state_fetch_all.py root root123 hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
