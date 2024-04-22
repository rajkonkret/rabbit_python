import pika
import sys

# fanout exchange - wiadomości zostają wysłane do wszystkich podpiętych kolejek
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# tworzenie exchanga
channel.exchange_declare(exchange='my-fanout-exchange', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hallo World"
channel.basic_publish(exchange='my-fanout-exchange', routing_key='', body=message)
print(f"Sent {message}")
connection.close()
