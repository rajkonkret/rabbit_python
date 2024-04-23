import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = "my-headers-exchange"
# exchange
channel.exchange_declare(exchange=exchange_name, exchange_type='headers', durable=True)

# kolejka
channel.queue_declare(queue="HealthQ", durable=True)
channel.queue_declare(queue="SportsQ", durable=True)
channel.queue_declare(queue="EducationQ", durable=True)

# binding (wiązania)
headers = {'x-match': 'any', 'h1': 'Header1', 'h2': 'Header2'}
channel.queue_bind(exchange=exchange_name, queue="HealthQ", routing_key='', arguments=headers)
headers = {'x-match': 'all', 'h1': 'Header1', 'h2': 'Header2'}
channel.queue_bind(exchange=exchange_name, queue="SportsQ", routing_key='', arguments=headers)
headers = {'x-match': 'any', 'h1': 'Header1', 'h2': 'Header2'}
channel.queue_bind(exchange=exchange_name, queue="EducationQ", routing_key='', arguments=headers)

print('Waiting for logs. To exit CTRL + C')


def callback(ch, method, properties, body, queue_name):
    print(f"{method}")
    print(f"{queue_name} routing_key: {method.routing_key}:{body}")


for q in ["HealthQ", "SportsQ", "EducationQ"]:
    print(f"Queue {q}")
    channel.basic_consume(
        queue=q,
        on_message_callback=lambda ch, method, properties, body, queue_name=q: callback(ch, method, properties, body,
                                                                                        queue_name),
        auto_ack=True
    )

channel.start_consuming()
