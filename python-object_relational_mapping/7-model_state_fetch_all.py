#!/usr/bin/python3
"""
Script that lists all State objects from a MySQL database using SQLAlchemy.

Usage:
    ./script.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to the database using SQLAlchemy
    - Retrieves all entries from the 'states' table
    - Prints the id and name of each State in the format: "<id>: <name>"

Example:
    ./script.py root root123 hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).all()

    for s in state:
        print("{}: {}".format(s.id, s.name))

    session.close()
