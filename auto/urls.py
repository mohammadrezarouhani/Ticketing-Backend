from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


user_router=DefaultRouter()
user_router.register('',views.UserViewSet)

letter_router=DefaultRouter()
letter_router.register('',views.LetterViewSet)

initial_letter_router=DefaultRouter()
initial_letter_router.register('',views.InitialLetterViewSet)

departman_router=DefaultRouter()
departman_router.register('',views.DepartmanViewSet)

message_router=DefaultRouter()
message_router.register('',views.CommentViewSet)

history=DefaultRouter()
history.register('',views.HistoryViewSet)


urlpatterns=[
    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    
    path('user/',include(user_router.urls),name='user-list'),# TODO check the problem of routing in app
    path('user/<str:pk>/',include(user_router.urls),name='user-detail'),
    path('change-password/<str:pk>/',views.ChangePasswordView.as_view(),name='change-password'),

    path('letter/',include(letter_router.urls),name='letter-list'),
    path('letter/<str:pk>/',include(letter_router.urls),name='letter-detail'),
    path('initial-letter/',include(initial_letter_router.urls),name='initial-letter'),

    path('departman/',include(departman_router.urls),name='departman'),

    path('comment/',include(message_router.urls),name='comment-list'),
    path('comment/<str:pk>/',include(message_router.urls),name='comment-detail'),
    path('comment-status/<str:pk>/',views.CommentStatusView.as_view(),name='comment-status'),
    
    path('history/',include(history.urls),name='history'),
    path('history/<int:pk>/',include(history.urls),name='history'),
]