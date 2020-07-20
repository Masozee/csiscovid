from django.urls import path, include, re_path
from covid import views as covidviews


urlpatterns = [
    path('', covidviews.Covid, name='covid-depekon'),
    path('index-mobility/', covidviews.indexMobility, name='mobility'),
    path('inflation-rates/', covidviews.inflationRates, name='inflation'),
    path('comodity/', covidviews.Comodity, name='comodity'),
    re_path('provinsi/(?P<Provinsi_slug>[\w-]+)/$', covidviews.provinsidetail, name='provinsi' )

]