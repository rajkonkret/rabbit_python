import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='my-topic-exchange', exchange_type='topic')

# tworzenie kolejek
channel.queue_declare(queue='HealthQ')
channel.queue_declare(queue='SportsQ')
channel.queue_declare(queue='EducationQ')

# binding
channel.queue_bind(exchange='my-topic-exchange', queue='HealthQ', routing_key='health.*')
channel.queue_bind(exchange='my-topic-exchange', queue='SportsQ', routing_key='#.sports.*')
channel.queue_bind(exchange='my-topic-exchange', queue='EducationQ', routing_key='#.education')

channel.close()
