import os
import sys

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callbacks(ch, method, properties, body):
        print(f"Recived {body}")

    channel.basic_consume(queue='hello', on_message_callback=callbacks, auto_ack=True)
    print("Waiting for message. CTRL-C exit")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
