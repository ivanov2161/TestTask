from django.contrib import admin
from .models import Mailing, Client, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'starttime', 'endtime', 'operatorcode', 'tag', 'message')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phonenumber', 'operatorcode', 'tag', 'utc')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sendtime', 'mailings_id', 'client_id', 'status')
