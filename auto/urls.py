from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

ticket_router=DefaultRouter()
ticket_router.register('',views.TicketViewSet)


ticket_message_router=DefaultRouter()
ticket_message_router.register('',views.TicketMessageViewSet)

ticket_history=DefaultRouter()
ticket_history.register('',views.TicketHistoryViewSet)

urlpatterns=[
    path('ticket/',include(ticket_router.urls)),
    path('ticket/<str:pk>/',include(ticket_router.urls)),

    path('ticket-message/',include(ticket_message_router.urls)),
    path('ticket-message/<str:pk>/',include(ticket_message_router.urls)),

    path('ticket-history/',include(ticket_history.urls)),
    path('ticket-history/<int:pk>/',include(ticket_history.urls)),
]