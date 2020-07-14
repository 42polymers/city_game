from django.contrib.auth.models import Group, User
from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .forms import EntryAdminForm
from .models import Entry


@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):

    form = EntryAdminForm
    default_lon = 9230747
    default_lat = 7367716
    default_zoom = 12
    list_display = ('name', 'image_tag', 'text',)


admin.site.unregister(Group)
admin.site.unregister(User)
