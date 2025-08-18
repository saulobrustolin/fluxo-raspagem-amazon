# consumer
import pika
from scrapping_product import scrapping_product

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='products_link', durable=True)

channel.basic_consume(
    queue='products_link', 
    on_message_callback=scrapping_product, 
    auto_ack=True,
    )

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
channel.start_consuming()
