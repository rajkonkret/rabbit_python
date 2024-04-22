import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severites = sys.argv[1:]
if not severites:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severites:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity
    )

print('Waiting for logs. To exit CTRL + C')


def callback(ch, method, properties, body):
    print(f"routing_key: {method.routing_key}:{body}")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True
)

channel.start_consuming()
