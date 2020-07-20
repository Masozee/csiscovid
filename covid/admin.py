from django.contrib import admin
from .models import Provinsi, kabkot, index, hargapangan, covid19provinsi


# Register your models here.
class ProvAdmin (admin.ModelAdmin):
    ordering = ['nama']
    list_display = ['nama','kode', 'ibukota']
    list_filter = ([])
    search_fields = ["nama", "ibukota" ]
    list_per_page = 25
admin.site.register(Provinsi, ProvAdmin)

class KotaAdmin (admin.ModelAdmin):
    ordering = ['nama']
    list_display = ['nama','kategori', 'provinsi']
    list_filter = (['kategori', 'provinsi'])
    search_fields = ["nama", "provinsi" ]
    list_per_page = 25

admin.site.register(kabkot, KotaAdmin)

class PanganAdmin (admin.ModelAdmin):
    ordering = ['tanggal']
    list_display = ['komoditas','tanggal', 'provinsi', 'harga']
    list_filter = (['komoditas', 'tanggal', 'harga'])
    search_fields = []
    list_per_page = 25

admin.site.register(hargapangan, PanganAdmin)

class CovidAdmin (admin.ModelAdmin):
    ordering = ['tanggal']
    list_display = ['provinsi','tanggal', 'terkonfirmasi','perawatan','sembuh','meninggal']
    list_filter = (['provinsi'])
    search_fields = []
    list_per_page = 25

admin.site.register(covid19provinsi, CovidAdmin)

class IndexAdmin (admin.ModelAdmin):
    ordering = ['tanggal']
    list_display = ['provinsi','tanggal', 'indexaktifkawalcovid','indexmovemennt',]
    list_filter = (['provinsi'])
    search_fields = []
    list_per_page = 25

admin.site.register(index, IndexAdmin)