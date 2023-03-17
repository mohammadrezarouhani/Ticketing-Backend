from .docs import letter_list_description
from . import permissions, serializer, models
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class ProfileViewset(RetrieveModelMixin,
                     UpdateModelMixin,
                     CreateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    permission_classes=[IsAuthenticated]
    queryset = models.Profile.objects.select_related('user').all()
    serializer_class = serializer.ProfileSerializer

    @action(detail=False,methods=['GET','PUT'])
    def me(self,request):
        (profile,created)=models.Profile.objects.get_or_create(user_id=request.user.id)
        if request.method=='GET':
            sre=serializer.ProfileSerializer(profile)
            return Response(sre.data)
        elif request.method=='PUT':
            sre=serializer.ProfileSerializer(profile,request.data)
            sre.is_valid(raise_exception=True)
            sre.save()
            return Response(sre.data)


@extend_schema_view(list=extend_schema(description=letter_list_description))
class LetterViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticated, permissions.LetterPermission]
    queryset = models.Letter.objects\
        .select_related('departman')\
        .select_related('sender')\
        .select_related('receiver').all()

    filter_backends = [DjangoFilterBackend]
    serializer_class = serializer.LetterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        sender = self.request.query_params.get('sender')
        receiver = self.request.query_params.get('receiver')
        departman = self.request.query_params.get('departman')
        status = self.request.query_params.get('status')

        if sender and receiver:
            queryset = queryset.filter(Q(sender=sender) | Q(receiver=receiver))
        elif sender:
            queryset = queryset.filter(Q(sender=sender))
        elif receiver:
            queryset = queryset.filter(Q(receiver=receiver))
        elif departman:
            queryset = queryset.filter(Q(departman=departman))
        elif status:
            queryset = queryset.filter(Q(status=status))

        return queryset


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, permissions.LetterMessagePermission]
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['letter', 'status']


class HistoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, permissions.HistoryPermission]
    serializer_class = serializer.History
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['owner', 'departman']
    search_fields = ['title']

    queryset = models.History.objects.prefetch_related('history_file').all()



class DepartmanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializer.DepartmanSerializer
    queryset = models.Departman.objects.all()


class CommentStatusView(RetrieveModelMixin,GenericViewSet):
    pass
    #TODO check acomment status is seen or unseen 


