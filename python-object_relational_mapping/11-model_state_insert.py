#!/usr/bin/python3
"""
Script that adds a new State object “Louisiana” to a MySQL database using
SQLAlchemy.

Usage:
    ./11-model_state_insert.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to the database using SQLAlchemy
    - Creates a new State with name="Louisiana"
    - Adds and commits it to the database
    - Prints the id of the newly created state

Example:
    ./11-model_state_insert.py root root123 hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("{}".format(new_state.id))

    session.close()
