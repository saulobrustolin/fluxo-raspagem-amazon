import psycopg2


def query_brand(brand, isregister):
    connect = psycopg2.connect(
        host="localhost",
        database="amazon",
        user="postgres",
        password="masterkey"
    )

    cursor = connect.cursor()

    sql = "INSERT INTO brand (name, isregister) VALUES (%s, %s)"
    values = (brand, isregister)

    cursor.execute(sql, values)

    connect.commit()

    print("Linha inserida com sucesso!")

    cursor.close()
    connect.close()
