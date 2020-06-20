from django.contrib.gis import forms
from django.utils.safestring import mark_safe

from .localization import ADMIN


class MapWidget(forms.OpenLayersWidget):

    template_name = 'map.html'
    name = 'map_widget'


class WorldBorderForm(forms.Form):
    world = forms.MultiPolygonField(widget=forms.OSMWidget(
        attrs={'map_width': 1024, 'map_height': 600}))


class EntryAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntryAdminForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ADMIN.get(field)

    # def image_preview(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.image.url,
    #         width=obj.image.width,
    #         height=obj.image.height,
    #         )
    # )

    def save(self, commit=True):
        instance = super(EntryAdminForm, self).save(commit=False)
        if not instance.point:
            raise Exception
        if commit:
            instance.save()
        return instance
