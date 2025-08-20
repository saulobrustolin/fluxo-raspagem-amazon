import psycopg2


def query_temp(obj):
    try:
        connect = psycopg2.connect(
            host="localhost",
            port=7000,
            database="amazon",
            user="amazon",
            password="amazon",
            options='-c client_encoding=UTF8'
        )

        cursor = connect.cursor()

        sql = "SELECT id FROM brand WHERE name = %s"

        cursor.execute(sql, (obj['brand'],))
        result = cursor.fetchone()

        sql = "INSERT INTO temp (link, brand) VALUES (%s, %s)"
        values = (obj['link'], result[0])

        cursor.execute(sql, values)

        connect.commit()

        cursor.close()
        connect.close()

        print(f"[insert_temp] Dados inseridos com sucesso na tabela 'temp'")
    except Exception as e:
        print(f"[insert_temp] Estou caindo no except: {e}")
