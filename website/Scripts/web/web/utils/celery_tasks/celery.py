from celery import Celery


broker = 'amqp://guest:guest@localhost:5672'
backend = 'redis://127.0.0.1:6379/3'


app = Celery('email', broker=broker, backend=backend,
             include=[
                 'celery_tasks.tasks',
             ])





