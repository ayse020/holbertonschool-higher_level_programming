#!/usr/bin/python3
"""
Script to fetch the first State object from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Main function to connect to the database and fetch the first State.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> \\")
        print("       <mysql password> <database name>")
        return

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Try mysql+mysqldb first (for checker), fall back to mysql+pymysql
        try:
            # Checker mysql+mysqldb gözləyir (mysqlclient)
            engine = create_engine(
                f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
                pool_pre_ping=True
            )
            # Test the connection
            conn = engine.connect()
            conn.close()
        except Exception:
            # Fall back to pymysql if mysqlclient not available
            engine = create_engine(
                f'mysql+pymysql://{username}:{password}@localhost:3306/{database}',
                pool_pre_ping=True
            )

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session instance
        session = Session()

        # Query the first State object ordered by id
        # Using .first() ensures we only fetch one record
        first_state = session.query(State).order_by(State.id).first()

        # Display the result
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
