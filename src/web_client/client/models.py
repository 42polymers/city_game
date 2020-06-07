from django.contrib.gis.db import models


class Entry(models.Model):
    point = models.PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', [])[::-1])
