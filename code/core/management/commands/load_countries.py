from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from countries.models import Country
from cities.models import City
from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

"""load countries and cities module"""

    

class Command(BaseCommand):
    """load countries and cities Command"""
    help = f"This command inserts cities and countries in database"

    def handle(self, *args, **options):
        world_shp = Path(__file__).resolve().parent.parent.parent / 'world_borders' / 'TM_WORLD_BORDERS-0.3.shp'
        print(f"world_shp={world_shp}")


        ds = DataSource(world_shp)
        print(ds)
        lyr = ds[0]
        print(lyr)

        
        countries_mapping = {
            'un' : 'UN',
            'name' : 'NAME',
            'lon' : 'LON',
            'lat' : 'LAT',
            'multi_polygone' : 'MULTIPOLYGON',
        }
        lm = LayerMapping(Country, world_shp, countries_mapping, transform=False)
        lm.save(strict=True, verbose=True)
         


#        number = options.get("number", 1)
#        seeder = Seed.seeder()
#        users = user_models.User.objects.all()
#        rooms = room_models.Room.objects.all()
#
#        seeder.add_entity(reservation_models.Reservation, number, {
#            "status": lambda x: random.choice(
#                ["pending", "confirmed", "canceled"]
#            ),
#            "check_in": lambda x: datetime.now(),
#            "check_out": lambda x: datetime.now()+timedelta(days=random.randint(3, 30)),
#            "guest": lambda x: random.choice(users),
#            "room": lambda x: random.choice(rooms),
#
#        })
#        seeder.execute()
#
#        self.stdout.write(
#            self.style.SUCCESS(f'{number} {NAME} created!')
#        )
