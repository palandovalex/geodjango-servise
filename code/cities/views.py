from django.core.serializers import deserialize
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .serializers import *
from .models import *


class CreatePhotoView(generics.CreateAPIView):
    serializer_class = PhotoDetailSerializer

    
class CityPhotoListView(generics.ListAPIView):
    serializer_class = PhotoListSerializer
    
    def get_queryset(self):
        city_pk = self.city_pk
        return City.objects.get(pk=city_pk).photos.objects.all()


class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoDetailSerializer
    queryset = Photo.objects.all()


class CreateCityView(generics.CreateAPIView):
    serializer_class = CityDetailSerializer

    
class CityListView(generics.ListAPIView):
    serializer_class = CityListSerializer
    
    def get_queryset(self):
        polygon_str = self.request.POST.get("polygon_filter")
        if polygon_str is None:
            return City.objects.all()
        
        polygon = deserialize("geojson", polygon_str)
        if isinstance(geom, str):
            raise ValidationError(polygon)
        return City.objects.all().filter(multi_polygon__contained=polygon)


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CityDetailSerializer
    queryset = City.objects.all()

