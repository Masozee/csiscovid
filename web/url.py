from django.urls import path, include, re_path
from web import views as webviews

urlpatterns = [
    path('', webviews.Covid, name='covid-depekon'),
]