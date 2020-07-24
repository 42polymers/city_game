from django.contrib.gis.db import models
from django.utils.safestring import mark_safe


class Entry(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    point = models.PointField()
    text = models.CharField(max_length=1000)
    map_part = models.ImageField(upload_to='map_parts')

    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', [])[::-1])

    def image_tag(self):
        return mark_safe(f'<img src="/{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
