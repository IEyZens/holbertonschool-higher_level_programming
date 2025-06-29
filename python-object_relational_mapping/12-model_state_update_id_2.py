#!/usr/bin/python3
"""
Script that updates the name of a State object in the database hbtn_0e_6_usa.

Usage:
    ./12-model_state_update_id_2.py <username> <password> <database>

Arguments:
    username  : MySQL username
    password  : MySQL password
    database  : name of the target database

Functionality:
    - Connects to a MySQL database using SQLAlchemy
    - Finds the State object with id = 2
    - Updates its name to "New Mexico"
    - Commits the change to the database

Example:
    ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
