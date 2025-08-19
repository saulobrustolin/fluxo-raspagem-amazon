import pika

def insert_in_rabbit(brand):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='brand_name', durable=True)

    channel.basic_publish(exchange='',
        routing_key='brand_name',
        body=brand,
        properties=pika.BasicProperties(
        delivery_mode=2
    ))
    print(f" [x] Produto enviado para fila 'brand_name'")

    connection.close()