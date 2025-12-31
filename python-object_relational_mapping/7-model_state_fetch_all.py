#!/usr/bin/python3
"""
Lists all State objects from database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py "
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create connection string
    # Format: mysql+mysqldb://username:password@localhost:3306/database_name
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    # Create engine to connect to the database
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    try:
        # Query all State objects and order by id in ascending order
        # Equivalent SQL: SELECT * FROM states ORDER BY id ASC
        states = session.query(State).order_by(State.id).all()

        # Display each state in the required format
        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        # Close the session
        session.close()
