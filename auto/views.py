from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from . import serializer
from . import models
import pdb

class TicketViewSet(ModelViewSet):
    serializer_class=serializer.TicketSerializer
    queryset=models.Ticket.objects.all()

    def get_queryset(self):
        data =super().get_queryset() 

        owner_id=self.request.query_params.get('owner','')
        departman_id=self.request.query_params.get('departman','')

        if owner_id:
            data=data.filter(owner__id=owner_id)

        if departman_id:
            data=data.filter(departman__id=departman_id)

        if owner_id or departman_id:
            return data


class TicketMessageViewSet(ModelViewSet):
    serializer_class=serializer.TicketMessageSerializer
    queryset=models.TicketMessage.objects.all()

    def get_queryset(self):
        data =super().get_queryset() 

        ticket_id=self.request.query_params.get('ticket','')

        if ticket_id:
            data=data.filter(ticket__id=ticket_id)
            return data


class TicketHistoryViewSet(ModelViewSet):
    serializer_class=serializer.TicketHistorySerializer
    queryset=models.TicketHistory.objects.all()

    def get_queryset(self):
        data=super().get_queryset()
        ticket_id=self.request.query_params.get('ticket','')
        if ticket_id:
            data.filter(ticket_id=ticket_id)
            return data