from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializer
from . import models

class TicketMessageViewSet(ModelViewSet):
    serializer_class=serializer.TicketSerializer
    queryset=models.Ticket.objects.all()
    

