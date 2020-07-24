import django_filters
from .models import ArtikelCov


class artikelFilter(django_filters.FilterSet):

    class Meta:
        model = ArtikelCov
        fields = {
            'judul': ['icontains'],
        }