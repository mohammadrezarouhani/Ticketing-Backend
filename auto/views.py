from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializer
from . import models


class DepartmanSerializerViewset(ModelViewSet):
    serializer_class=serializer.DepartmanSerializer
    queryset=models.Departman.objects.all()

    
class TicketViewSet(ModelViewSet):
    serializer_class=serializer.TicketSerializer
    queryset=models.Ticket.objects.all()


class TicketMessage(ModelViewSet):
    serializer_class=serializer.TicketMessageSerializer
    queryset=models.TicketMessage.all()


class TicketHistoryViewSet(ModelViewSet):
    serializer_class=serializer.TicketHistorySerializer
    queryset=models.TicketHistory.all()
