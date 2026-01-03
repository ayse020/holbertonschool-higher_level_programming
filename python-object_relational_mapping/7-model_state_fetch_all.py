#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Script arqumentlərini oxumaq
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Arqumentləri dəyişənlərə mənimsətmək
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # MySQL serverinə qoşulma
        db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
        engine = create_engine(
            db_url.format(username, password, database),
            pool_pre_ping=True
        )

        # Session yaratmaq
        Session = sessionmaker(bind=engine)
        session = Session()

        # Bütün State obyektlərini sıralamaq
        states = session.query(State).order_by(State.id).all()

        # Nəticələri ekrana çap etmək
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Sessionu bağlamaq
        session.close()

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)
