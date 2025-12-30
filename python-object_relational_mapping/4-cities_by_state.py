#!/usr/bin/python3
"""
4-cities_by_state.py
MySQLdb modulu ile verilenler bazasından
seherleri statlarla birlikde çıxaran skript
"""

import MySQLdb
import sys


def main():
    """Esas icra funksiyası"""
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py "
              "<mysql_username> <mysql_password> <database_name>")
        return

    # Giriş arqumentlerini oxuyuruq
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # MySQL serverine bağlantı qururuq
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
        )

        # Kursor yaradırıq
        cursor = db.cursor()

        # SQL sorğusunu tertib edirik
        # Seherler ve statları birleşdiririk
        sql_query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """

        # Sorğunu icra edirik (yalnız bir defe execute())
        cursor.execute(sql_query)

        # Butun neticeleri elde edirik
        results = cursor.fetchall()

        # Neticeleri formatda çap edirik
        for row in results:
            print(row)

        # Kursor ve bağlantını bağlayırıq
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
