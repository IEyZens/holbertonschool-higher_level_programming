#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username : MySQL username
    mysql_password : MySQL password
    database_name  : Name of the database to connect to

Functionality:
    - Connects to the database using SQLAlchemy
    - Retrieves and displays all State objects with 'a' in their name
    - Results are sorted by ascending State.id

Example:
    ./9-model_state_filter_a.py root root hbtn_0e_6_usa
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
        .order_by(State.id)
        .filter(State.name.like("%a%"))
        .all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
