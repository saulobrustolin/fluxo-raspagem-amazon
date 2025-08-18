import psycopg2

def query(table, campos, values):
    connect = psycopg2.connect(
        host="localhost",
        database="amazon",
        user="postgres",
        password="masterkey"
    )

    cursor = connect.cursor()

    # tratamentos
    campos = ", ".join(campos);
    values = ", ".join(values);

    sql = "INSERT INTO %s (%s) VALUES (%s)"
    values = (table, campos, values)

    cursor.execute(sql, values)

    connect.commit()

    print("Linha inserida com sucesso!")

    cursor.close()
    connect.close()
