"""automation_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', include('auto.urls')),
    path('file/',include('file.urls')),
]

# django_doc_urlpatterns=[
#     path('doc/',include_docs_urls(title="Automation")),
#     path('schema',get_schema_view(
#         title="Automation App",
#         description="Api for ticketing app",
#         version="1.0.0",
#         )
#         ,name="automation-api"
#     ),    
# ]
 
spectacular_urlpatterns=[
    path('schema/',SpectacularAPIView.as_view(),name='schema'),
    path('doc/',SpectacularSwaggerView.as_view(url_name='schema'),name='doc')
]

debug_toolbar_urlpatterns=[
    path('__debug__',include('debug_toolbar.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # urlpatterns.extend(django_doc_urlpatterns)
    urlpatterns.extend(spectacular_urlpatterns)
    urlpatterns.extend(debug_toolbar_urlpatterns)
