#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
Takes 4 arguments: mysql username, mysql password, database name and state name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        msg = "Usage: {} <mysql username> <mysql password> "
        msg += "<database name> <state name>"
        print(msg.format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create cursor
        cursor = db.cursor()

        # SQL query with parameter to prevent SQL injection
        # Using single execute() as required
        query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        # Execute query with state name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Extract city names from results
        cities_list = [row[0] for row in results]

        # Print cities separated by comma and space
        print(", ".join(cities_list))

        # Close cursor and database
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
