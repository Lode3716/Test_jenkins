"""
   
 auth : l.devigne
lancer le serveur celery sous windows = celery -A tp09.tasks_celery worker --loglevel=INFO -P solo
"""
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//', backend="redis://localhost:6379/0")


@app.task
def add(x, y):
    return x + y
