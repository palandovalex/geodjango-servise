from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from countries.models import Country
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

"""load countries and cities module"""

    

class Command(BaseCommand):
    """load countries and cities Command"""
    help = f"This command inserts cities and countries in database"

    def handle(self, *args, **options):

        countries = Country.objects.all()


        

#        self.stdout.write(
#            self.style.SUCCESS(f'{number} {NAME} created!')
#        )
