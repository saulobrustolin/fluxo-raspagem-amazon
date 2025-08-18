# consumer.py
import pika

def callback(ch, method, properties, body):
    print(f"[x] Recebido")

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila (mesmo nome do producer)
channel.queue_declare(queue='products_link', durable=True)

# Diz para o RabbitMQ chamar a função callback quando receber uma mensagem
channel.basic_consume(
    queue='products_link', 
    on_message_callback=callback, 
    auto_ack=True,
    )

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
channel.start_consuming()
