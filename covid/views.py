import json
import urllib
import requests

from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import hargapangan, covid19provinsi, Provinsi, ArtikelCov, Subscribe
from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .filters import artikelFilter
from .forms import EmailSignupForm


# Create your views here.
def Count(request):
    return render(request, 'countdown.html')

def Covid(request):
    return render(request, 'covid/index.html')

def indexMobility(request):
    return render(request, 'covid/mobility.html')

def inflationRates(request):
    return render(request, 'covid/inflasi.html')

def Comodity(request):
    return render(request, 'covid/comodity.html')

def kontak(request):
    return render(request, 'covid/kontak.html')

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

def ArtikelList(request,):
    artikel = ArtikelCov.objects.all()
    paginator = Paginator(artikel, 9)

    page = request.GET.get('page')
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)

    context = {
        "artikel": artikel,
    }

    return render(request, 'covid/artikel.html', context)

def enCovid(request):
    return render(request, 'coviden/index.html')

def enindexMobility(request):
    return render(request, 'coviden/mobility.html')

def eninflationRates(request):
    return render(request, 'coviden/inflasi.html')

def enComodity(request):
    return render(request, 'coviden/comodity.html')

def enkontak(request):
    return render(request, 'coviden/kontak.html')

def enprovinsi_json(request,  Provinsi_nama):
    harga = hargapangan.objects.get(provinsi=Provinsi_nama)
    json = serializers.serialize('json', harga)
    context ={
        "json": json,
    }

    return HttpResponse(context, content_type='application/json')

def enprovinsidetail(request, Provinsi_slug):
    prov = Provinsi.objects.get(slug=Provinsi_slug)

    context = {
        "prov": prov,
    }

    return render(request, 'coviden/provinsi.html', context)

def enArtikelList(request,):
    artikel = ArtikelCov.objects.all()
    paginator = Paginator(artikel, 5)

    page = request.GET.get('page')
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)

    context = {
        "artikel": artikel,
    }

    return render(request, 'coviden/articles.html', context)

#SUBSCRIBE FUNCTION
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)

def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = Subscribe.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))