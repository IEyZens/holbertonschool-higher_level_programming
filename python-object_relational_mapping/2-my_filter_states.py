#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Connects to a MySQL server running on localhost at port 3306.
Uses format to create the SQL query with the user input.
Results are sorted in ascending order by states.id.
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
        "SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC"
        .format(sys.argv[4])
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
