#!/usr/bin/python3
"""
Script that safely displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password>
    <database_name> <state_name>

Connects to a MySQL server running on localhost at port 3306.
Uses parameterized queries to prevent SQL injection.
Results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], db=sys.argv[3]
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute a safe query using parameter substitution to avoid SQL injection
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id ASC",
        (sys.argv[4],))

    # Print each matching row
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
