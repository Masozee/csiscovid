from django.contrib import admin
from django.urls import path, include, re_path
from users import views as userviews
from web import views as webviews
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('covid.url') ),
    path('', include('gsheets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)