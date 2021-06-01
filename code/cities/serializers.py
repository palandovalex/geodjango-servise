from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import City, Photo


class PhotoDetailSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ("caption", "city", "file") 


class PhotoListSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ("pk", "caption", "city", "get_url")


class CityDetailSerializer(GeoModelSerializer):
    class Meta:
        model = City
        fields = ("name", "description", "point", "multi_polygon")


class CityListSerializer(GeoModelSerializer):
    class Meta:
        model = City
        fields = ("pk", "name", "point")
