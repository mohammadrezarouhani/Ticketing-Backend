from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

admin.site.site_header="Automation Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', include('auto.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
 
spectacular_urlpatterns=[
    path('schema/',SpectacularAPIView.as_view(),name='schema'),
    path('doc/',SpectacularSwaggerView.as_view(url_name='schema'),name='doc')
]

debug_toolbar_urlpatterns=[
    path('__debug__',include('debug_toolbar.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns.extend(spectacular_urlpatterns)
    urlpatterns.extend(debug_toolbar_urlpatterns)
