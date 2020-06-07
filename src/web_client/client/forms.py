from django.contrib.gis import forms


class MapWidget(forms.OpenLayersWidget):

    template_name = 'map.html'
    name = 'map_widget'


class WorldBorderForm(forms.Form):
    world = forms.MultiPolygonField(widget=forms.OSMWidget(
        attrs = {'map_width': 1024, 'map_height': 600}))
