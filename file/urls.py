from django.urls import path,include
from . import views


urlpatterns=[
    path('file-upload/',views.FileUploadAPiView.as_view(),name='comment-status')
]