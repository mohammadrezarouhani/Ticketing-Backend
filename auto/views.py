from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import permissions,serializer,models
import pdb


class UserViewSet(ModelViewSet):

    serializer_class=serializer.BaseUserSerializer
    queryset=models.BaseUser.objects.all()

    def get_permissions(self):
        if not self.request.method == 'POST':
            self.permission_classes=[IsAuthenticated,]
        return super().get_permissions()

    def create(self,request,*args,**kwargs):
        sre=self.get_serializer(data=request.data)

        if(sre.is_valid()):
            sre.save()
            return Response(sre.data,status=status.HTTP_201_CREATED)
        
        return Response(sre.errors,status=status.HTTP_201_CREATED)


class TicketViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,permissions.TicketPermission]
    serializer_class=serializer.LetterSerializer
    queryset=models.Letter.objects.all()

    def list(self, request, *args, **kwargs):
        data =self.get_queryset()

        owner_id=self.request.query_params.get('owner','')
        departman_id=self.request.query_params.get('departman','')

        if (owner_id or departman_id) :
            data=data.filter(Q(owner__id=owner_id)|Q(departman__id=departman_id))
            sre=self.get_serializer(data,many=True)
            return Response(data=sre.data,status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketMessageViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,permissions.TicketMessagePermission]
    serializer_class=serializer.LetterCommentSerializer
    queryset=models.LetterMessage.objects.all()

    def list(self, request, *args, **kwargs):
        data =self.get_queryset()
        ticket_id=self.request.query_params.get('ticket','')

        if ticket_id :
            data=data.filter(ticket__id=ticket_id)
            sre=self.get_serializer(data,many=True)
            return Response(data=sre.data,status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketHistoryViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,permissions.TicketHistoryPermission]
    serializer_class=serializer.TicketHistorySerializer
    queryset=models.History.objects.all()

    def list(self, request, *args, **kwargs):
        data =self.get_queryset()

        ticket_id=self.request.query_params.get('ticket','')
        
        if ticket_id:
            data=data.filter(ticket__id=ticket_id)
            sre=self.get_serializer(data,many=True)
            return Response(data=sre.data,status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmanViewSet(ModelViewSet):
    http_method_names=['get']
    permission_classes=[IsAuthenticated,]
    
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


class MessageStatusView(generics.UpdateAPIView,):
    permission_classes=[IsAuthenticated]
    serializer_class=serializer.CommentStatusSerializer
    model=models.BaseUser


    def update(self, request, *args, **kwargs):
        message_id=request.data.get('comment_id')
        user_id=self.kwargs.get('pk')

        if user_id == request.user.id:
            message_obj=get_object_or_404(models.LetterMessage,id=message_id)
            user_obj=get_object_or_404(models.BaseUser,id=user_id)

            if message_obj.status=='US':
                user_obj.has_message -=1
                message_obj.status='SN'
                user_obj.save()
                message_obj.save()
                return Response(status=status.HTTP_200_OK)
            return Response(data={"status":"comment already been seen"},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data={"status":"wrong user id or comment id"},status=status.HTTP_404_NOT_FOUND)