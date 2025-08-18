# producer.py
import pika
import time

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila (se não existir)
channel.queue_declare(queue='minha', durable=True)

# Envia mensagens
while True:
    for i in range(5):
        mensagem = f"Mensagem {i+1}"
        channel.basic_publish(exchange='',
                            routing_key='minha_fila',
                            body=mensagem)
        print(f" [x] Enviado: {mensagem}")
        time.sleep(2)
    time.sleep(5)

# Fecha a conexão
# connection.close()
