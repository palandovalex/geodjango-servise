from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from core import models as core_models


class Country(core_models.TimeStampedModel):
    name = models.CharField(max_length=128, unique=True)
    capital = models.OneToOneField("cities.City", related_name="+", on_delete=models.PROTECT, null=True)
    un = models.IntegerField('United Nations Code')
    point = models.PointField(default=Point(0,0))
    multi_polygon = models.MultiPolygonField()
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
