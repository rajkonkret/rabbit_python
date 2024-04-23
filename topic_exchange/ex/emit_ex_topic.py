import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# tworzymy exchange
channel.exchange_declare(exchange='my-topic-exchange', exchange_type='topic')

message = "Hallo world"
routing_key = "sports.sports.sports"
channel.basic_publish(
    exchange='my-topic-exchange', routing_key=routing_key, body=message
)

print(f"Sent: {routing_key}:{message}")
connection.close()
