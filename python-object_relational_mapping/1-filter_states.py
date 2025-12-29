#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Main function that connects to the database and executes the query.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N'
        # Using BINARY to make the comparison case-sensitive for 'N'
        query = """
        SELECT id, name
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC
        """
        cursor.execute(query)

        # Fetch all results
        results = cursor.fetchall()

        # Print each row
        for row in results:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)


# Ensure script only runs when executed directly, not when imported
if __name__ == "__main__":
    main()
