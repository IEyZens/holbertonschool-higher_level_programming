#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Connects to a MySQL server running on localhost at port 3306.
Retrieves all cities and their associated state names.
Results are sorted in ascending order by cities.id.
Uses only one execute() statement.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
