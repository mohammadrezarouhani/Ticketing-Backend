from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,status
from rest_framework.response import Response
from .permissions import TicketPermission
from . import serializer
from . import models
import pdb

class TicketViewSet(ModelViewSet):
    permission_classes=[TicketPermission,]
    serializer_class=serializer.TicketSerializer
    queryset=models.Ticket.objects.all()


    def list(self, request, *args, **kwargs):
        data =self.get_queryset()

        owner_id=self.request.query_params.get('owner','')
        departman_id=self.request.query_params.get('departman','')

        if owner_id or departman_id:
            data=data.filter(Q(owner__id=owner_id)|Q(departman__id=departman_id))
            sre=self.get_serializer(data,many=True)
            return Response(data=sre.data,status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketMessageViewSet(ModelViewSet):
    permission_classes=[]
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


class DepartmanViewSet(ModelViewSet):
    http_method_names=['get']

    serializer_class=serializer.DepartmanSerializer
    queryset=models.Departman.objects.all()


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class=serializer.ChangePasswordSerializer
    model=models.BaseUser

    def get_object(self):
        return get_object_or_404(models.BaseUser,pk=self.kwargs['pk'])


    def update(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        user=self.get_object()

        if serializer.is_valid():
            
            if not user.check_password(serializer.data.get('old_password')):
                return Response(data={'password':'old password is wrong!'},status=status.HTTP_204_NO_CONTENT)
            try:
                validate_password(serializer.data.get('new_password'))
            except Exception as ex:
                return Response(data={'password':ex},status=status.HTTP_406_NOT_ACCEPTABLE)

            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

