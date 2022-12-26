from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


user_router=DefaultRouter()
user_router.register('',views.UserViewSet)

letter_router=DefaultRouter()
letter_router.register('',views.TicketViewSet)

initial_letter_router=DefaultRouter()
initial_letter_router.register('',views.InitialTicketViewSet)

departman_router=DefaultRouter()
departman_router.register('',views.DepartmanViewSet)

letter_message_router=DefaultRouter()
letter_message_router.register('',views.TicketMessageViewSet)

letter_history=DefaultRouter()
letter_history.register('',views.TicketHistoryViewSet)


urlpatterns=[
    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    
    path('user/',include(user_router.urls)),
    path('user/<str:pk>/',include(user_router.urls)),
    path('change-password/<str:pk>/',views.ChangePasswordView.as_view()),

    path('letter/',include(letter_router.urls)),
    path('letter/<str:pk>/',include(letter_router.urls)),
    path('initial-letter/',include(initial_letter_router.urls)),

    path('departman/',include(departman_router.urls)),

    path('comment/',include(letter_message_router.urls)),
    path('comment/<str:pk>/',include(letter_message_router.urls)),
    path('comment-status/<str:pk>/',views.MessageStatusView.as_view()),
    
    path('history/',include(letter_history.urls)),
    path('history/<int:pk>/',include(letter_history.urls)),
]