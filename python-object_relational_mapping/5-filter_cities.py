#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database
hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Connects to a MySQL server running on localhost at port 3306.
Retrieves all cities that belong to the specified state
(provided as the fourth argument).
Results are sorted in ascending order by cities.id.
Uses a parameterized query to prevent SQL injection.
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
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC", (sys.argv[4],)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
