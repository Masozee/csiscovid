from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import hargapangan, covid19provinsi, Provinsi


# Create your views here.
def Covid(request):
    return render(request, 'covid/index.html')

def indexMobility(request):
    return render(request, 'covid/mobility.html')

def inflationRates(request):
    return render(request, 'covid/inflasi.html')

def Comodity(request):
    return render(request, 'covid/comodity.html')

def provinsi_json(request,  Provinsi_nama):
    harga = hargapangan.objects.get(provinsi=Provinsi_nama)
    json = serializers.serialize('json', harga)
    context ={
        "json": json,
    }

    return HttpResponse(context, content_type='application/json')

def provinsidetail(request, Provinsi_slug):
    prov = Provinsi.objects.get(slug=Provinsi_slug)

    context = {
        "prov": prov,
    }

    return render(request, 'covid/provinsi.html', context)

    return