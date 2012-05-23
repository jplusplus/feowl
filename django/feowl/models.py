#rom django.db import models
from django.contrib.gis.db import models


class HelloWorld(models.Model):
    text_1 = models.CharField(max_length=200)
    text_2 = models.CharField(max_length=200)
    int_1 = models.IntegerField()
    geographic_point_1 = models.PointField(srid=4326, geography=True, blank=True)
    date_1 = models.DateTimeField('date insert')
