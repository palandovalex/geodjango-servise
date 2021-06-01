from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from countries.models import Country
from cities.models import City
from django.contrib.gis.gdal import DataSource

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'world_borders' / 'TM_WORLD_BORDERS-0.3.shp'
print(f"world_shp={world_shp}")

def run(verbose=True):
    #lm = LayerMapping(Country, world_shp, world_mapping, transform=False)
    #lm.save(strict=True, verbose=verbose)
    ds = DataSource(world_shp)
    print(ds)
