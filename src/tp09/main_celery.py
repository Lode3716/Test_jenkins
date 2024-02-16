"""
   
 auth : l.devigne

"""
from celery import Celery, signature


def main():
    app = Celery('tasks', broker='amqp://guest@localhost//', backend="redis://localhost:6379/0")
    add_task = signature('tp09.tasks_celery.add')
    add = add_task.delay(2, 3)
    print(add.get())


if __name__ == '__main__':
    main()
