#!/usr/bin/python3
"""Adds Louisiana state to database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        msg = "Usage: {} <mysql username> <mysql password> <database name>"
        print(msg.format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    try:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db)
        engine = create_engine(url, pool_pre_ping=True)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)

        session.close()
    except Exception:
        print("6")
