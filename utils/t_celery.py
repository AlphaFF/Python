from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost//')


@app.task(name='task.add')
def add(x, y):
    return x + y


if __name__ == '__main__':
    for i in range(5):
        r = add.delay(i, i + 10)
