from InterviewTask.celery import app
from .models import Mailing, Client, Message
from celery import shared_task
from datetime import datetime
import requests
import pytz

URL = 'https://probe.fbrq.cloud/v1/send/'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI0Mjk0MjEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImthdHVsbF9pdnkifQ.VARCHml8sapPc0ipstcfYOTt0niGes7N1luXrLQ-iMI'
header = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'}

timezone = pytz.timezone('UTC')


@app.task
def send_message(mailing_id, client_id):
    mailing = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    data = {
        "id": mailing.pk,
        "phone": client.phonenumber,
        "text": mailing.message
    }
    res = requests.post(url=URL + str(data['id']), headers=header, json=data)
    if res:
        Message.objects.create(status=True, mailings_id=mailing, client_id=client)
    else:
        Message.objects.create(status=False, mailings_id=mailing, client_id=client)


@ shared_task(name='check_mailings')
def check_mailings():
    mailings = Mailing.objects.all()
    clients = Client.objects.all()
    timenow = datetime.now(timezone)
    for mailing in mailings:
        for client in clients:
            if client.operatorcode == mailing.operatorcode and client.tag == mailing.tag:
                if mailing.starttime < timenow < mailing.endtime:
                    send_message(mailing.pk, client.pk)


def test():
    mailings = Mailing.objects.set_all()
    for mail in mailings:
        print(mail)