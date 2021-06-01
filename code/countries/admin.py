from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": (
                "name", "capital", "point", 
                 "un", "multi_polygon"
            )}
        ),
    )

    ordering = ("name", )

    list_display = (
        "name",
        "capital",
        "point",
        "un",
    )

    list_filter = (
        "name",
    )

    def count_cities(self, obj):
        return obj.cities.count()
    count_cities.short_description = "Cities count"
