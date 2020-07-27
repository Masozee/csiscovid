from django.urls import path, include, re_path
from covid import views as covidviews


urlpatterns = [
    path('', covidviews.Count, name='countdown'),
    path('home', covidviews.Covid, name='covid-depekon'),
    path('index-mobilitas/', covidviews.indexMobility, name='mobility'),
    path('tingkat-inflasi/', covidviews.inflationRates, name='inflation'),
    path('komoditas/', covidviews.Comodity, name='comodity'),
    path('kontak/', covidviews.kontak, name='kontak'),
    path('artikel/', covidviews.ArtikelList, name='artikel'),
    path('en/home/', covidviews.enCovid, name='en-covid-depekon'),
    path('en/mobility-index/', covidviews.enindexMobility, name='en-mobility'),
    path('en/inflation-rates/', covidviews.eninflationRates, name='en-inflation'),
    path('en/commodities/', covidviews.enComodity, name='en-comodity'),
    path('en/contact/', covidviews.enkontak, name='en-kontak'),
    path('en/articles/', covidviews.enArtikelList, name='en-artikel'),


    #english


    re_path('provinsi/(?P<Provinsi_slug>[\w-]+)/$', covidviews.provinsidetail, name='provinsi' )

]