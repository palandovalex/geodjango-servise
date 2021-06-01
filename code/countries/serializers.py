from rest_framework_gis.serializers import GeoModelSerializer
from .models import Country


class CountryDetailSerializer(GeoModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryListSerializer(GeoModelSerializer):
    class Meta:
        model = Country
        fields = ("pk", "name", "point")
