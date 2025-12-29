#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to MySQL database and lists all states sorted by id
    """
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Execute SQL query to get all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Display results
        for row in rows:
            print(row)
        
        # Close cursor and connection
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Main execution block - only runs when script is executed directly
    """
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the function to list states
    list_states(username, password, database)
