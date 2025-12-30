#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections.
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and execute safe query
    """
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create cursor object
        cursor = db.cursor()

        # Create SAFE SQL query using parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the query with parameter
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Display results
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


# Prevent execution when imported
if __name__ == "__main__":
    main()
