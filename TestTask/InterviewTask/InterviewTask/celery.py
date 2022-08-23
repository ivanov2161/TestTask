import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InterviewTask.settings')

app = Celery('InterviewTask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_message-every-30-seconds': {
        'task': 'send',
        'schedule': 30.0,
        'args': (3, 3)
    },
}
app.conf.timezone = 'UTC'
