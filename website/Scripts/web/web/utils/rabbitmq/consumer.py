import pika

credentials = pika.plaincredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParamters('localhost', 5672, '/',credentials))
channel = connection.channel()
channel.queue_declare(queue='EmailCode')

#定义队列接受消息的回调函数

def callback(channel, method,properties,body):
    print(body)

channel.basic_consume(queue='EmailCode', auto_ack=True, on_message_callback=callback)
channel.start_consuming()