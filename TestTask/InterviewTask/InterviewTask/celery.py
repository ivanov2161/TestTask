import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InterviewTask.settings')

app = Celery('InterviewTask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_mailings-every-30-seconds': {
        'task': 'check_mailings',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'UTC'
