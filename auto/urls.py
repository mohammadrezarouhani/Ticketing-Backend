from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

ticket_router=DefaultRouter()
ticket_router.register('',views.TicketViewSet)

departman_router=DefaultRouter()
departman_router.register('',views.DepartmanSerializerViewset)

ticket_message_router=DefaultRouter()
ticket_message_router.register('',views.TicketMessageViewSet)

ticket_history=DefaultRouter()
ticket_history.register('',views.TicketHistoryViewSet)
urlpatterns=[
    path('ticket/',include(ticket_router.urls)),
    path('ticket/<int:pk>/',include(ticket_router.urls)),

    path('departman/',include(departman_router.urls)),
    path('departman/<int:pk>/',include(departman_router.urls)),

    path('ticket-message/',include(ticket_message_router.urls)),
    path('ticket-message/<int:pk>/',include(ticket_message_router.urls)),

    path('ticket-history/',include(ticket_history.urls)),
    path('ticket-history/<int:pk>/',include(ticket_history.urls)),
]