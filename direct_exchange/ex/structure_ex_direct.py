import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='my-direct-exchange', exchange_type='direct')

queues = ['MobileQ', 'ACQ', 'LightQ']
for queue in queues:
    channel.queue_declare(queue=queue)

channel.queue_bind(exchange='my-direct-exchange', queue='MobileQ', routing_key='personalDevice')
channel.queue_bind(exchange='my-direct-exchange', queue='ACQ', routing_key='homeAppliance')
channel.queue_bind(exchange='my-direct-exchange', queue='MobileQ', routing_key='homeAppliance')

channel.close()
