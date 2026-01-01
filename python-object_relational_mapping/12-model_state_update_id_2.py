#!/usr/bin/python3
"""
Skript: State obyektinin adını yeniləmək
Məqsəd: id-si 2 olan State obyektinin adını "New Mexico" olaraq dəyişdirmək
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Arqumentləri oxumaq
    if len(sys.argv) != 4:
        print("İstifadə: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # 2. MySQL server-ə qoşulmaq
    # .format() metodu ilə - daha uyğun format
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    
    # 3. Session yaratmaq
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # 4. id-si 2 olan State obyektini tapmaq
        state_to_update = session.query(State).filter(State.id == 2).first()
        
        # 5. Əgər obyekt tapsa, onu yeniləmək
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
            print("State obyekti uğurla yeniləndi!")
        else:
            print("Xəta: id-si 2 olan State obyekti tapılmadı")
    
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
        session.rollback()
    
    finally:
        # 6. Session-u bağlamaq
        session.close()
