from django.contrib import admin
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "point", "multi_polygon")}
        ),
    )

    ordering = ("name", )

    list_display = (
        "name",
        "country",
        "point",
        )

    list_filter = (
        "country",
    )

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photos count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="75px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
