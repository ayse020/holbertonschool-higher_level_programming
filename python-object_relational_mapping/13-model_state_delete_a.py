#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
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

        # 'a' hərfi olan bütün State obyektlərini tapmaq
        states_to_delete = session.query(State).filter(
            State.name.like('%a%')
        ).all()

        # Hər bir tapılan obyekti silmək
        for state in states_to_delete:
            session.delete(state)

        # Dəyişiklikləri yadda saxlamaq
        session.commit()

        # Sessionu bağlamaq
        session.close()

        print("States containing 'a' have been deleted successfully.")

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)
