import pika
from pika import SelectConnection


def on_open(connection):
    connection.channel(on_channel_open)


channel = None


def on_channel_open(channel_):
    global channel
    channel = channel_
    channel.queue_declare(queue='example_queue', callback=on_queue_declared)


def on_queue_declared(frame):
    channel.basic_publish(
        exchange='',
        routing_key='example_queue',
        body='Hallo World!'
    )

    print("Message sent")
    connection.close()


parameters = pika.ConnectionParameters(host='localhost')
connection = SelectConnection(parameters, on_open_callback=on_open)

try:
    connection.ioloop.start()
except KeyboardInterrupt:
    connection.close()
    connection.ioloop.close()
