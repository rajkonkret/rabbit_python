from functools import partial

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='my-topic-exchange', exchange_type='topic')

channel.queue_declare(queue='HealthQ')
channel.queue_declare(queue='SportsQ')
channel.queue_declare(queue='EducationQ')

# binding
channel.queue_bind(exchange='my-topic-exchange', queue='HealthQ', routing_key='health.*')
channel.queue_bind(exchange='my-topic-exchange', queue='SportsQ', routing_key='#.sports.*')
channel.queue_bind(exchange='my-topic-exchange', queue='EducationQ', routing_key='#.education')


def callback(ch, method, properties, body, queue_name):
    print(f"{method}")
    print(f"{queue_name} routing_key: {method.routing_key}:{body}")


queues = ["HealthQ", 'SportsQ', 'EducationQ']
# channel.basic_consume(queue="HealthQ", on_message_callback=callback, auto_ack=True)
# channel.basic_consume(queue="HealthQ", on_message_callback=callback, auto_ack=True)
# channel.basic_consume(queue="HealthQ", on_message_callback=callback, auto_ack=True)

for q in queues:
    # z wykorzystaniem partial()
    # queue_callback = partial(callback, queue_name=q)
    # channel.basic_consume(
    #     queue=q, on_message_callback=queue_callback, auto_ack=True
    # )

    # z wykorzystaniem lambdy
    channel.basic_consume(
        queue=q,
        on_message_callback=lambda ch, method, properties, body, queue_name=q: callback(ch, method, properties, body,
                                                                                        queue_name),
        auto_ack=True

    )

print("Starting consume")
channel.start_consuming()
