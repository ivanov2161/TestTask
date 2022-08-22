from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class MailingAPI(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        queryset = Message.objects.filter(mailings_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullstats(self, request):
        total_count = Mailing.objects.count()
        mailing = Mailing.objects.values('id')
        content = {'Total number of mailings': total_count,
                   'The number of messages sent': ''}
        out = {}

        for row in mailing:
            res = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
            mail = Message.objects.filter(mailings_id=row['id']).all()
            status_true = mail.filter(status=True).count()
            status_false = mail.filter(status=False).count()
            res['Total messages'] = len(mail)
            res['True'] = status_true
            res['False'] = status_false
            out[row['id']] = res

        content['The number of messages sent'] = out
        return Response(content)


class ClientAPI(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageAPI(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
