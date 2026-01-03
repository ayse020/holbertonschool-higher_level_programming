#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

        # Bütün City obyektlərini state adı ilə birlikdə çıxarmaq
        # JOIN istifadə edərək State və City cədvəllərini birləşdiririk
        results = session.query(City, State).filter(
            City.state_id == State.id
        ).order_by(City.id).all()

        # Nəticələri ekrana çap etmək
        for city, state in results:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        # Sessionu bağlamaq
        session.close()

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)
