import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# tworenie exchange
channel.exchange_declare(exchange='my-fanout-exchange', exchange_type='fanout')

# tworzenie kolejek
channel.queue_declare(queue='MobileQ')
channel.queue_declare(queue='ACQ')
channel.queue_declare(queue='LightQ')

# tworzenie bindingów
channel.queue_bind(exchange='my-fanout-exchange', queue='MobileQ')
channel.queue_bind(exchange='my-fanout-exchange', queue='ACQ')
channel.queue_bind(exchange='my-fanout-exchange', queue='LightQ')

channel.close()
