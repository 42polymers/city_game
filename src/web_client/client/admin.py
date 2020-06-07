from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):

    default_lon = 9230747
    default_lat = 7367716
    default_zoom = 12
