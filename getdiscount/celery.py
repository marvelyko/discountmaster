import os
from celery import Celery
from celery.schedules import crontab

app = Celery("getdiscount",backend="amqp",broker="amqp://")

app.config_from_object("django.conf:settings",namespace="CELERY")

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-30-second': {
        'task': 'main.tasks.check',
        'schedule': 30.0,
    },
}

app.autodiscover_tasks()