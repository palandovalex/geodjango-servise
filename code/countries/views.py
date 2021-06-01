from django.core.serializers import deserialize
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from countries.serializers import *
from countries.models import Country
from cities.serializers import CityListSerializer


class CreateCountryView(generics.CreateAPIView):
    serializer_class = CountryDetailSerializer

    
class CountryListView(generics.ListAPIView):
    serializer_class = CountryListSerializer
    
    def get_queryset(self):
        polygon_str = self.request.POST.get("polygon_filter")
        if polygon_str is None:
            return Country.objects.all()
        
        polygon = deserialize("geojson", polygon_str)
        if isinstance(geom, str):
            raise ValidationError(polygon)
        return Country.objects.all().filter(multi_polygon__contained=polygon)



class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CountryDetailSerializer
    queryset = Country.objects.all()


class CountryCitiesListView(generics.ListAPIView):
    serializer_class = CityListSerializer

    def get_queryset(self):
        country_pk = self.pk
        country = Country.objects.get(pk=country_pk)
        return country.cities.objects.all()
