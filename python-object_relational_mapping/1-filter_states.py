#!/usr/bin/python3
"""
Script that lists all states starting with 'N' from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

Connects to a MySQL server running on localhost at port 3306.
Retrieves all states with names starting with 'N' (uppercase), ordered by
states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using provided credentials
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print all matching rows
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
