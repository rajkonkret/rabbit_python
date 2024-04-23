import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# exchange
channel.exchange_declare(exchange="exchange-test", exchange_type='headers', durable=True)

# kolejka
channel.queue_declare(queue="headers_queue", durable=True)

# binding (wiązania)
headers = {'x-match': 'all', 'category': 'novel', 'format': 'hardcover'}
channel.queue_bind(exchange="exchange-test", queue="headers_queue", routing_key='', arguments=headers)

headers = {'category': 'novel', 'format': 'hardcover'}
properties = pika.BasicProperties(headers=headers)
channel.basic_publish(exchange="exchange-test", routing_key='', body="Text", properties=properties)
print("Message sent with headers")


def callback(ch, method, properties, body):
    print(f"Recived: {body.decode()}")


channel.basic_consume(queue="headers_queue", on_message_callback=callback, auto_ack=True)

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming()
