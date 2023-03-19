from django.urls import path,include
from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter
from . import views



routers=DefaultRouter()
routers.register('profile',views.ProfileViewset,basename='profile')
routers.register('letter',views.LetterViewset,basename='letter')
routers.register('departman',views.DepartmanViewset,basename='departman')
routers.register('archive',views.ArchiveViewset,basename='history')
routers.register('message',views.MessageViewset,basename='message')

archive_router=NestedDefaultRouter(routers,'archive',lookup='archive')
archive_router.register('file',views.ArchiveFileViewset,basename='Archive-file')

message_router=NestedDefaultRouter(routers,'message',lookup='message')
message_router.register('file',views.MessageFileViewset,basename='message-file')

urlpatterns=[
    path('',include(routers.urls)),
    path('',include(archive_router.urls)),
]
