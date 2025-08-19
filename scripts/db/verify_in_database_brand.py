import psycopg2

def verify_in_database_brand(brand):
    connect = psycopg2.connect(
        host="localhost",
        database="amazon",
        user="postgres",
        password="masterkey"
    )

    cursor = connect.cursor()

    sql = "SELECT isregistred FROM brand WHERE brand = %s"

    cursor.execute(sql, brand)

    result = cursor.fetchone()

    print("Linha inserida com sucesso!")

    cursor.close()
    connect.close()

    if result:
        return result[0]
    else:
        return None
