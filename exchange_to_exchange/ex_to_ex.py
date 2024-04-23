import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

source_exchange = 'source_exchange'
destination_exchange = 'destination_exchange'
channel.exchange_declare(exchange=source_exchange, exchange_type='direct')
channel.exchange_declare(exchange=destination_exchange, exchange_type='fanout')

routing_key = 'example_routing_key'

channel.exchange_bind(destination=destination_exchange, source=source_exchange, routing_key=routing_key)

message = 'Hello, Exchange to Exchange'
channel.basic_publish(exchange=source_exchange, routing_key=routing_key, body=message)
print(f"Sent '{message}' to exchange {source_exchange} with routing_key {routing_key}")

queue_name = 'final_queue'
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(queue=queue_name, exchange=destination_exchange, routing_key='')


def callback(ch, method, properties, body):
    print(f"Received {body.decode('utf-8')}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for messages")
channel.start_consuming()
