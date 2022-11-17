from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

ticket_message_router=DefaultRouter()
ticket_message_router.register('',views.TicketMessageViewSet)

urlpatterns=[
    path('ticket-message/',include(ticket_message_router.urls)),
    path('ticket-message/<int:pk>/',include(ticket_message_router.urls)),
]