# consumer
import pika
from scripts.product.scrapping_product import scrapping

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',
    heartbeat=65535,
    blocked_connection_timeout=65535
    ))
channel = connection.channel()

channel.queue_declare(queue='products_link', durable=True)

channel.basic_consume(
    queue='products_link', 
    on_message_callback=scrapping, 
    auto_ack=True,
    )

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
channel.start_consuming()
