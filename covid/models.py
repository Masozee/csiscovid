from django.db import models
import datetime
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase, TaggedItemBase
from gsheets import mixins
from uuid import uuid4

# Create your models here.
class Provinsi(models.Model):
    nama = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    kode = models.CharField(max_length=3)
    ibukota = models.CharField(max_length=30, blank=True)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Provinsi")
        verbose_name_plural = ("Provinsi")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class kabkot(models.Model):
    KATEGORI_CHOICES = (
        ('Kabupaten', 'Kabupaten'),
        ('Kota', 'Kota')
    )

    provinsi = models.ForeignKey(Provinsi, on_delete=models.PROTECT)
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES)
    nama = models.TextField(max_length=100)
    slug = models.SlugField(default='', editable=False, max_length=140)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = ("kabupaten/kota")
        verbose_name_plural = ("kabupaten/kota")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.kategori + self.nama

class covid19provinsi(models.Model):
    tanggal = models.DateField(default=datetime.date.today)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.PROTECT)
    slug = models.SlugField(default='', editable=False, max_length=140)
    terkonfirmasi = models.IntegerField()
    perawatan = models.IntegerField()
    sembuh = models.IntegerField()
    meninggal = models.IntegerField()

    class Meta:
        verbose_name = ("Pasien Provinsi")
        verbose_name_plural = ("pasien Provinsi")

    def save(self, *args, **kwargs):
        value = str(self.provinsi)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.provinsi)

class hargapangan(models.Model):
    KOMODITAS_CHOICES = (
        ('Beras', 'Beras'),
        ('Daging Ayam', 'Daging Ayam'),
        ('Daging Sapi', 'Daging Sapi'),
        ('Telur Ayam', 'Telur Ayam'),
        ('Bawang Merah', 'Bawang Merah'),
        ('Bawang Putih', 'Bawang Putih'),
        ('Cabai Merah', 'Cabai Merah'),
        ('Cabai Rawit', 'Cabai Rawit'),
        ('Minyak Goreng', 'Minyak Goreng'),
        ('Gula Pasir', 'Gula Pasir'),
    )

    
    komoditas = models.CharField(max_length=30, choices=KOMODITAS_CHOICES, default = 'Beras')
    tanggal = models.DateField(default=datetime.date.today)
    slug = models.SlugField(default='', editable=False, max_length=140)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.PROTECT)
    harga = models.IntegerField()
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Harga Pangan")
        verbose_name_plural = ("harga Pangan")

    def save(self, *args, **kwargs):
        value = self.komoditas
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.komoditas

class index(models.Model):
    tanggal = models.DateField(default=datetime.date.today)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.PROTECT)
    indexaktifkawalcovid = models.DecimalField(max_digits=19, decimal_places=10)
    indexmovemennt = models.DecimalField(max_digits=19, decimal_places=10)

    class Meta:
        verbose_name = ("Index")
        verbose_name_plural = ("indexes")

    def __str__(self):
        return str(self.provinsi)


class Author(TagBase):
    ket = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Author")

class TaggedAuthor(GenericTaggedItemBase):
    tag = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items",
    )
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Author")

class topikArtikel(models.Model):
    nama = models.CharField(max_length=30)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Topik")
        verbose_name_plural = ("Topik")

    def __str__(self):
        return self.nama


class ArtikelCov(models.Model):
    judul = models.CharField(max_length=70)
    slug =models.SlugField(default='', editable=False, max_length=140)
    tanggal = models.DateField()
    topik = models.ForeignKey(topikArtikel, on_delete=models.CASCADE)
    authors = TaggableManager(through=TaggedAuthor, related_name='abstracts', verbose_name='Author')
    image = models.URLField(blank=True)
    file = models.URLField(blank=True)
    tag = TaggableManager()
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Artikel")
        verbose_name_plural = ("Artikel")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Subscribe(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
