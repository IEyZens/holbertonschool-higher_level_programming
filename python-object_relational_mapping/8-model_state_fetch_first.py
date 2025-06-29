#!/usr/bin/python3
"""
Script that prints the first State object from a MySQL database using SQLAlchemy.

Usage:
    ./8-model_state_fetch_first.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to the database using SQLAlchemy
    - Retrieves and displays the first State object by id
    - If no state exists, prints 'Nothing'

Example:
    ./8-model_state_fetch_first.py root root123 hbtn_0e_6_usa
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

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
