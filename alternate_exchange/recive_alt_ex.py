import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(f"Body: {body}")


channel.basic_consume(queue='ae_queue', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
