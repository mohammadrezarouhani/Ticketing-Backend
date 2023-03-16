from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views



router=DefaultRouter()
router.register(r'letter',views.LetterViewSet,basename='letter')
router.register(r'initial-letter',views.InitialLetterViewSet,basename='initial-letter')
router.register(r'departman',views.DepartmanViewSet,basename='departman')
router.register(r'comment',views.CommentViewSet,basename='comment')
router.register(r'history',views.HistoryViewSet,basename='history')


urlpatterns=[
    path('',include(router.urls),name='user'),
]
