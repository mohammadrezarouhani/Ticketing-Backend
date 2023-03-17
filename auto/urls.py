from django.urls import path,include
from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter
from . import views



routers=DefaultRouter()
routers.register(r'profile',views.ProfileViewset,basename='profile')
routers.register(r'letter',views.LetterViewset,basename='letter')
routers.register(r'departman',views.DepartmanViewset,basename='departman')
routers.register(r'history',views.HistoryViewset,basename='history')

Letter_router=NestedDefaultRouter(routers,'letter',lookup='letter')
Letter_router.register('comment',views.CommentViewset)

urlpatterns=[
    path('',include(routers.urls)),
    path('',include(Letter_router.urls)),
]
