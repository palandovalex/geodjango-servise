from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from core import models as core_models


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=140)
    file = models.ImageField(upload_to="room_photos")
    city = models.ForeignKey(
        "City", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    def get_url(self):
        return self.file.url

    class Meta:
        verbose_name = "Photo"


class City(core_models.TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    country = models.ForeignKey(
            "countries.Country", related_name="cities", 
            on_delete=models.SET_NULL, blank=True, null=True
    )
    point = models.PointField(default=Point(0,0))
    multi_polygon = models.MultiPolygonField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        city_point = self.point
        city_shape = self.multi_polygon
        country = self.country
        if not country.multi_polygon.contains(city_point):
            raise ValueError("incorrect point")
        
        if not country.multi_polygon.contains(city_shape):
            raise ValueError("incorrect city shape")

        super().save(self, *args, **kwargs)

        

    class Meta:
        verbose_name_plural = "Cities"
