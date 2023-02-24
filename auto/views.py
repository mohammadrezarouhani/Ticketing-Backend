from django.shortcuts import get_object_or_404
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from drf_spectacular.utils import extend_schema_view,extend_schema
from . import permissions,serializer,models
from .docs import letter_list_description


class UserViewSet(ModelViewSet):
    http_method_names=['get','delete']
    permission_classes=[IsAuthenticated]
    serializer_class=serializer.BaseUserSerializer
    queryset=models.BaseUser.objects.select_related('departman').all()


class UserUpdateView(ModelViewSet):
    http_method_names=['put']
    permission_classes=[IsAuthenticated]
    serializer_class=serializer.UpdateUserSerializer
    queryset=models.BaseUser.objects.select_related('departman').all()      
    
    
class UserCreateView(ModelViewSet):
    http_method_names=['post']
    permission_classes=[IsAuthenticated]
    serializer_class=serializer.CreateUserSerializer
    queryset=models.BaseUser.objects.select_related('departman').all()       


@extend_schema_view(list=extend_schema(description=letter_list_description))
class LetterViewSet(ModelViewSet):
    http_method_names=['get','put','delete']
    permission_classes=[IsAuthenticated,permissions.LetterPermission]
    queryset=models.Letter.objects\
        .select_related('departman')\
        .select_related('sender')\
        .select_related('receiver').all()
        
    filter_backends=[DjangoFilterBackend]
    serializer_class=serializer.LetterSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        sender=self.request.query_params.get('sender')
        receiver=self.request.query_params.get('receiver')
        departman=self.request.query_params.get('departman')
        status=self.request.query_params.get('status')
        if sender:
            queryset=queryset.filter(Q(sender=sender))
        elif receiver:
            queryset=queryset.filter(Q(receiver=receiver))
        elif sender and  receiver:
            queryset=queryset.filter(Q(sender=sender)|Q(receiver=receiver))
        elif departman:
            queryset=queryset.filter(Q(departman=departman))
        elif status:
            queryset=queryset.filter(Q(status=status))
        else:
            return queryset


class InitialLetterViewSet(ModelViewSet):
    http_method_names=['post','get']
    permission_classes=[IsAuthenticated,permissions.LetterPermission]
    serializer_class=serializer.InitialLetterSerializer
    queryset=models.Letter.objects.all()


class CommentViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,permissions.LetterMessagePermission]
    serializer_class=serializer.CommentSerializer
    queryset=models.Comment.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['letter','status']
    
    
class HistoryViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,permissions.HistoryPermission]
    serializer_class=serializer.History
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=['owner','departman']
    search_fields=['title']
    
    queryset=models.History.objects\
        .prefetch_related('history_file')\
        .select_related('owner')\
        .select_related('departman').all()


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


class CommentStatusView(generics.UpdateAPIView,):
    permission_classes=[IsAuthenticated]
    serializer_class=serializer.CommentStatusSerializer
    model=models.BaseUser


    def update(self, request, *args, **kwargs):
        comment_id=request.data.get('comment')
        user_id=self.kwargs.get('pk')

        if user_id == request.user.id:
            message_obj=get_object_or_404(models.Comment,id=comment_id)
            user_obj=get_object_or_404(models.BaseUser,id=user_id)
            

            if message_obj.status=='US':
                user_obj.has_message -=1
                message_obj.status='SN'
                user_obj.save()
                message_obj.save()
                return Response(data={"status":"comment was seen by {}".format(user_obj.username)},status=status.HTTP_200_OK)
            return Response(data={"status":"comment has been seen before"},status=status.HTTP_200_OK)
        
        return Response(data={"status":"wrong user id or comment id"},status=status.HTTP_404_NOT_FOUND)


class TokenDetailView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=models.BaseUser.objects.select_related('departman').all()
    serializer_class=serializer.BaseUserSerializer

    def list(self, request, *args, **kwargs):
        user=request.user
        sre=self.get_serializer(user)
        return Response(data=sre.data)