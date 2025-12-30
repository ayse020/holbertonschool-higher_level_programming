#!/usr/bin/python3
"""
Script to create the states table in the database
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create connection string
    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database
    )
    
    try:
        # Create engine and connect to database
        engine = create_engine(connection_string, pool_pre_ping=True)
        
        # Create all tables defined in Base's metadata
        Base.metadata.create_all(engine)
        
        print("Table 'states' created successfully in database '{}'!".format(database))
        
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
