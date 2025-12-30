#!/usr/bin/python3
"""
4-cities_by_state.py
MySQLdb modulu ilə verilənlər bazasından şəhərləri ştatlarla birlikdə çıxaran skript
"""

import MySQLdb
import sys

def main():
    """Əsas icra funksiyası"""
    if len(sys.argv) != 4:
        print("İstifadə: ./4-cities_by_state.py <mysql_istifadəçi> <mysql_parol> <verilənlər_bazası_adı>")
        return
    
    # Giriş arqumentlərini oxuyuruq
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    try:
        # MySQL serverinə bağlantı qururuq
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
        )
        
        # Kursor yaradırıq
        cursor = db.cursor()
        
        # SQL sorğusunu tərtib edirik
        # Şəhərlər və ştatları birləşdiririk, ştat_id üzərindən JOIN edirik
        sql_query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        
        # Sorğunu icra edirik (yalnız bir dəfə execute())
        cursor.execute(sql_query)
        
        # Bütün nəticələri əldə edirik
        results = cursor.fetchall()
        
        # Nəticələri formatda çap edirik
        for row in results:
            print(row)
        
        # Kursor və bağlantını bağlayırıq
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print(f"MySQL xətası: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Xəta: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
