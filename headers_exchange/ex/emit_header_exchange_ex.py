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

headers = {'h1': 'Header1', 'h2': 'Header23'}
properties = pika.BasicProperties(headers=headers)
channel.basic_publish(exchange=exchange_name, routing_key='', body="Message for Headers Exchange h1,h2, H23", properties=properties)
print("Message sent with headers")

connection.close()