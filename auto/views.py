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
from .docs import letter_list_description,user_list_description



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
        
        if sender and  receiver:
            queryset=queryset.filter(Q(sender=sender)|Q(receiver=receiver))
        elif sender: 
            queryset=queryset.filter(Q(sender=sender))
        elif receiver:
            queryset=queryset.filter(Q(receiver=receiver))
        elif departman:
            queryset=queryset.filter(Q(departman=departman))
        elif status:
            queryset=queryset.filter(Q(status=status))
        
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
    http_method_names=['get'] #TODO  change this to mixin why using model viewset???
    permission_classes=[IsAuthenticated,]
    
    serializer_class=serializer.DepartmanSerializer
    queryset=models.Departman.objects.all()
