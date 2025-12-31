#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> \\")
        print("       <mysql password> <database name> <state name>")
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Create engine to connect to the database
        # Try mysql+mysqldb first (for checker), fall back to mysql+pymysql
        try:
            conn_str = (f'mysql+mysqldb://{username}:{password}@'
                        f'localhost:3306/{database}')
            engine = create_engine(conn_str, pool_pre_ping=True)
            conn = engine.connect()
            conn.close()
        except Exception:
            conn_str = (f'mysql+pymysql://{username}:{password}@'
                        f'localhost:3306/{database}')
            engine = create_engine(conn_str, pool_pre_ping=True)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session instance
        session = Session()

        # Query the State object with the given name
        # Using == operator is safe from SQL injection with SQLAlchemy
        state = session.query(State).filter(State.name == state_name).first()

        # Display the result
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
