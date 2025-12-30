#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Uses MySQLdb module and format to create SQL query.
"""

import MySQLdb
import sys

def main():
    """
    Main function to connect to database and execute query
    """
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        return
    
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
        
        # Create SQL query using format() as required
        # IMPORTANT: In real applications, use parameterized queries instead!
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        
        # Execute the query
        cursor.execute(query)
        
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
