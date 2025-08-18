import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="meu_banco",
    user="meu_usuario",
    password="minha_senha"
)

cursor = conexao.cursor()

sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
valores = ("Saulo Brustolin", "saulo@email.com")

cursor.execute(sql, valores)

conexao.commit()

print("Linha inserida com sucesso!")

cursor.close()
conexao.close()
