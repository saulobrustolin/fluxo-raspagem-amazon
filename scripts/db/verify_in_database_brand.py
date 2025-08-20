import psycopg2

def verify_in_database_brand(brand):
    try:
        connect = psycopg2.connect(
            host="localhost",
            port=7000,
            database="amazon",
            user="amazon",
            password="amazon",
        )

        cursor = connect.cursor()

        sql = "SELECT isregister FROM brand WHERE name = %s"

        cursor.execute(sql, (str(brand),))

        result = cursor.fetchone()

        cursor.close()
        connect.close()

        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print('[verify_in_database_brand] Estou caindo no except:', e)
        return None
