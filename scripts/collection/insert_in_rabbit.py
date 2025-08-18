import pika

def insert_in_rabbit(link_product):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='products_link', durable=True)

    channel.basic_publish(exchange='',
        routing_key='products_link',
        body=link_product,
        properties=pika.BasicProperties(
        delivery_mode=2
    ))
    print(f" [x] Produto enviado para fila 'products_link'")

    connection.close()