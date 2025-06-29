#!/usr/bin/python3
"""
Script that prints the id of a State object with a given name from a
MySQL database using SQLAlchemy.

Usage:
    ./10-model_state_my_get.py <username> <password> <database> <state_name>

Arguments:
    username     : MySQL username
    password     : MySQL password
    database     : Name of the target database
    state_name   : Name of the State to search for

Functionality:
    - Connects to the database using SQLAlchemy
    - Searches for a State object with the exact name given
    - Prints the id of the matching State object
    - If no match is found, prints "Not found"

Example:
    ./10-model_state_my_get.py root root123 hbtn_0e_6_usa Texas
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

    state = (
        session.query(State)
        .order_by(State.id)
        .filter(State.name == sys.argv[4])
        .first()
    )

    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
