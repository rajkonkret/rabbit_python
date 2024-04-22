import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.exchange_declare(exchange='my-direct-exchange', exchange_type='direct')

queues = ['MobileQ', 'ACQ', 'LightQ']
for queue in queues:
    channel.queue_declare(queue=queue)

channel.queue_bind(exchange='my-direct-exchange', queue='MobileQ', routing_key='personalDevice')
channel.queue_bind(exchange='my-direct-exchange', queue='ACQ', routing_key='homeAppliance')
channel.queue_bind(exchange='my-direct-exchange', queue='MobileQ', routing_key='homeAppliance')

print('Waiting for logs. To exit CTRL + C')


def callback(ch, method, properties, body):
    print(f"{method}")
    print(f"routing_key: {method.routing_key}:{body}")


for q in queues:
    print(f"Queue {q}")
    channel.basic_consume(
        queue=q, on_message_callback=callback, auto_ack=True
    )

channel.start_consuming()
