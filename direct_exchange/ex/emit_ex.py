import pika
import sys

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# tworzymy exchange
channel.exchange_declare(exchange='my-direct-exchange', exchange_type='direct')

message = "Hello World"
routing_key = "homeAppliance"
channel.basic_publish(
    exchange='my-direct-exchange', routing_key=routing_key, body=message)

print(f"Sent: {routing_key}:{message}")
connection.close()
