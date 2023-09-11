import pika

credentials = pika.plaincredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParamters('localhost', 5672, '/',credentials))
channel = connection.channel()
channel.queue_declare(queue='EmailCode')
channel.basic_publish(exchange='', routing_key='EmailCode', body=b'verification')
connection.close()
