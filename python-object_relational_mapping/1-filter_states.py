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
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
