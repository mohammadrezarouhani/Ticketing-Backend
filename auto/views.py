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


class TicketMessageViewSet(ModelViewSet):
    serializer_class=serializer.TicketMessageSerializer
    queryset=models.TicketMessage.objects.all()


class TicketHistoryViewSet(ModelViewSet):
    serializer_class=serializer.TicketHistorySerializer
    queryset=models.TicketHistory.objects.all()
