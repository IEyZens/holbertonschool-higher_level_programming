#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa,
sorted by city id in ascending order.

Usage:
    ./14-model_city_fetch_by_state.py <username> <password> <database>

Arguments:
    username    : MySQL username
    password    : MySQL password
    database    : Name of the target database

Functionality:
    - Connects to a MySQL database using SQLAlchemy
    - Retrieves all City objects and their associated State
    - Prints each city in the format: <state name>: (<city id>) <city name>

Note:
    The script should not execute its logic when imported as a module.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    for citie, state in cities:
        print("{}: {} {}".format(state.name, citie.id, citie.name))

    session.close()
