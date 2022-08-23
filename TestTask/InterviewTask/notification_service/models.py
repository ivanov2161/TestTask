from django.db import models


class Mailing(models.Model):
    starttime = models.DateTimeField()
    message = models.TextField()
    operatorcode = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)
    endtime = models.DateTimeField()


class Client(models.Model):
    phonenumber = models.IntegerField()
    operatorcode = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)
    utc = models.CharField(max_length=10)


class Message(models.Model):
    sendtime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    mailings_id = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
