import psycopg2


def query_brand(brand, isregister):
    connect = psycopg2.connect(
        host="localhost",
        port=7000,
        database="amazon",
        user="amazon",
        password="amazon",
        options='-c client_encoding=UTF8'
    )

    cursor = connect.cursor()

    sql = "INSERT INTO brand (name, isregister) VALUES (%s, %s)"
    values = (brand, isregister)

    cursor.execute(sql, values)

    connect.commit()

    print(f"Salvei a marca '{brand}' com o status de registro: {isregister}")

    cursor.close()
    connect.close()
