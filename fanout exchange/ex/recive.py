import pika
from threading import Thread


def callback(ch, method, properties, body):
    # print(f" Recived from {method.routing_key}: {body.decode()}\n")
    print(f" Recived from {method}: {body.decode()}\n")


def consume_queue(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(f"Starting to consume from {queue_name}\n")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        channel.close()
        print(f"Stopped consuming from {queue_name}")


if __name__ == '__main__':
    queues = ['MobileQ', 'ACQ', 'LightQ']
    threads = []

    for queue in queues:
        thread = Thread(target=consume_queue, args=(queue,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
