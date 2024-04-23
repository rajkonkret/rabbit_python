import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

ae_exchange = "my-ae"
channel.exchange_declare(exchange=ae_exchange, exchange_type='fanout', durable=True)

main_exchange = 'my-main-exchange'
channel.exchange_declare(
    exchange=main_exchange, exchange_type='direct', durable=True, arguments={'alternate-exchange': ae_exchange})

main_queue = "main-queue"
channel.queue_declare(queue=main_queue, durable=True)
channel.queue_bind(queue=main_queue, exchange=main_exchange, routing_key='key1')

ae_queue = 'ae_queue'
channel.queue_declare(queue=ae_queue, durable=True)
channel.queue_bind(queue=ae_queue, exchange=ae_exchange, routing_key='')

channel.basic_publish(exchange=main_exchange, routing_key='key1', body='message')
channel.basic_publish(exchange=main_exchange, routing_key='nonexistent_key', body='Alternate Exchange')

connection.close()
