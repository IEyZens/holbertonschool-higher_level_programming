#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

This script connects to a MySQL server running on localhost at port 3306
and retrieves all rows from the 'states' table, ordered by states.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database using credentials passed as arguments
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        password=sys.argv[2], db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute SQL query to select all states ordered by their ID
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch and print all rows from the executed query
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
