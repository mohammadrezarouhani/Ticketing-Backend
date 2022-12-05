from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


user_router=DefaultRouter()
user_router.register('',views.UserViewSet)

ticket_router=DefaultRouter()
ticket_router.register('',views.TicketViewSet)

departman_router=DefaultRouter()
departman_router.register('',views.DepartmanViewSet)

ticket_message_router=DefaultRouter()
ticket_message_router.register('',views.TicketMessageViewSet)

ticket_history=DefaultRouter()
ticket_history.register('',views.TicketHistoryViewSet)

urlpatterns=[
    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    
    path('user/',include(user_router.urls)),
    path('user/<str:pk>/',include(user_router.urls)),
    path('change-password/<str:pk>/',views.ChangePasswordView.as_view()),

    path('ticket/',include(ticket_router.urls)),
    path('ticket/<str:pk>/',include(ticket_router.urls)),

    path('departman/',include(departman_router.urls)),

    path('ticket-message/',include(ticket_message_router.urls)),
    path('ticket-message/<str:pk>/',include(ticket_message_router.urls)),
    path('message-status/<str:pk>/',views.MessageStatusView.as_view()),
    
    path('ticket-history/',include(ticket_history.urls)),
    path('ticket-history/<int:pk>/',include(ticket_history.urls)),
]