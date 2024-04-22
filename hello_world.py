import pika

# stworzyc połaczenie
# stworzyc kanał
# stworzyc kolejkę
# wysłąć wiadomość

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# alt ctrl l - formatuje kod
# dostosowuje do zasad PEP8

# stworzenie kolejki
channel.queue_declare(queue='hello')

# wysłanie wiadomości
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body="Hello World!!!")

print("Wysłano wiadomość")
connection.close()
