from . import permissions, serializer, models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ProfileViewset(GenericViewSet):

    permission_classes = [IsAuthenticated]
    queryset = models.Profile.objects.select_related('departman').all()
    serializer_class = serializer.ProfileSerializer

    @extend_schema(request=serializer.ProfileSerializer, methods=['GET'])
    @extend_schema(request=serializer.UpdateProfileSerializer, methods=['PUT'])
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        profile = get_object_or_404(models.Profile, user_id=request.user.id)
        if request.method == 'GET':
            sre = serializer.ProfileSerializer(profile)
            return Response(sre.data)
        elif request.method == 'PUT':
            sre = serializer.ProfileSerializer(profile, request.data)
            sre.is_valid(raise_exception=True)
            sre.save()
            return Response(sre.data)


class LetterViewset(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):
    permission_classes = [IsAuthenticated, permissions.LetterPermission]
    queryset = models.Letter.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']
    serializer_class = serializer.LetterSerializer

    @action(detail=False, methods=['GET'])
    def me(self, request):
        letters = models.Letter.objects.filter(
            Q(sender_id=request.user.id) | Q(receiver_id=request.user.id))
        sre = serializer.LetterSerializer(letters, many=True)
        return Response(sre.data)


class MessageViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, permissions.LetterMessagePermission]
    serializer_class = serializer.MessageSerializer
    queryset = models.Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['letter', 'status']


class MessageFileViewset(ModelViewSet):
    queryset = models.MessageFile
    serializer_class = serializer.MessageFileserializer

    def get_serializer_context(self):
        return {'message_pk': self.kwargs['message_pk']}

    def get_queryset(self):
        return super().get_queryset().filter(message=self.kwargs['message_pk'])


class ArchiveViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, permissions.HistoryPermission]
    serializer_class = serializer.History
    filter_backends = [SearchFilter]
    search_fields = ['title']
    queryset = models.Archive.objects.all()


class ArchiveFileViewset(ModelViewSet):
    queryset = models.ArchiveFile.objects.all()
    serializer_class = serializer.ArchiveFileSerializer

    def get_queryset(self):
        return super().get_queryset().filter(archive_id=self.kwargs.get('archive_pk'))

    def get_serializer_context(self):
        return {'archive_pk': self.kwargs['archive_pk']}


class DepartmanViewset(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializer.DepartmanSerializer
    queryset = models.Departman.objects.all()


class MessageStatusViewset(CreateModelMixin, GenericViewSet):
    serializer_class = serializer.MessageStatusSerializer

    def create(self, request, *args, **kwargs):
        sre = serializer.MessageStatusSerializer(data=request.data)
        sre.is_valid(raise_exception=True)
        user_id = sre.data.get('user_id')
        message = get_object_or_404(models.Message, id=kwargs['message_pk'])
        profile = get_object_or_404(models.Profile, user_id=user_id)

        if message.status == 'UN':
            message.status = 'SN'
            profile.has_message -= 1
            message.save()
            profile.save()
            return Response('message {} was seen by {}'.format(message.id, user_id))
        else:
            return Response(data={'message {}  was seend before by user {} '.format(message.id, user_id)},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
