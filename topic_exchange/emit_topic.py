# topic exchange
# routing ustalany na podstawie patternu
# * - dokłądnie jedno słowo
# # (hash) - zero lub więcej słów
# . - oddziela słowa

import pika
import sys

# tworzenie połaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# tworzenie exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)

print(f" [x] Sent {message} with routing key {routing_key}")
connection.close()
