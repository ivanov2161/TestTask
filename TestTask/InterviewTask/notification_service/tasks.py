from InterviewTask.celery import app
from .models import Mailing, Client, Message
from celery import shared_task
from datetime import datetime
import requests
from celery.utils.log import get_task_logger
import pytz
import logging

logger = get_task_logger(__name__)
URL = 'https://probe.fbrq.cloud/v1/send/'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI0Mjk0MjEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImthdHVsbF9pdnkifQ.VARCHml8sapPc0ipstcfYOTt0niGes7N1luXrLQ-iMI'
header = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'}


# @app.task
@ shared_task(name='send')
def send_message(mailing_id, client_id):
    mailing = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    data = {
        "id": mailing.pk,
        "phone": client.phonenumber,
        "text": mailing.message
    }
    # res = requests.post(url=URL + str(data['id']), headers=header, json=data)
    print('test')
    Message.objects.create(status=True, mailings_id=mailing, client_id=client)



# app.conf.beat_schedule = {
#     'send_message-every-30-seconds': {
#         'task': 'notification_service.tasks.send_message',
#         'schedule': 30.0,
#         'args': (3, 3)
#     },
# }
# app.conf.timezone = 'UTC'


# timezone = pytz.timezone('UTC')
# time = datetime.now(timezone)
# print(time)
