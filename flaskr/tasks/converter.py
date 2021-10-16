from ..models import db
from celery import Celery
from celery.signals import task_postrun


app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task()
def convert_file(data):
    pass

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()
