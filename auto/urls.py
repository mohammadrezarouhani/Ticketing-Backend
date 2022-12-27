from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


router=DefaultRouter()
router.register(r'user',views.UserViewSet,basename='user')
router.register(r'letter',views.LetterViewSet,basename='letter')
router.register(r'initial-letter',views.InitialLetterViewSet,basename='initial-letter')
router.register(r'departman',views.DepartmanViewSet,'departman')
router.register(r'comment',views.CommentViewSet,'comment')
router.register(r'history',views.HistoryViewSet,'history')


urlpatterns=[
    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('change-password/<str:pk>/',views.ChangePasswordView.as_view(),name='change-password'),
    path('',include(router.urls),name='user'),
    path('comment-status/<str:pk>/',views.CommentStatusView.as_view(),name='comment-status')
]