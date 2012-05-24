#rom django.db import models
from django.contrib.gis.db import models


class HelloFeowl(models.Model):
    text_1 = models.CharField(max_length=200)
    text_2 = models.CharField(max_length=200)
    int_1 = models.IntegerField()

    #SRID 4326 is WGS84 is lon/lat
    #stay with geometries since they support more postgis functions
    #see: http://postgis.refractions.net/documentation/manual-1.5/ch04.html#PostGIS_GeographyVSGeometry
    geographic_point_1 = models.PointField(srid=4326, geography=False, blank=True, help_text="String of form POINT(lon, lat)")
    
    date_1 = models.DateTimeField()
    
    def __unicode__(self):
          return self.text_1

