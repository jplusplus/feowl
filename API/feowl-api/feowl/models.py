#rom django.db import models
from django.contrib.gis.db import models
#from jsonfield import JSONField

class Report(models.Model):
  createdAt = models.DateTimeField()
  modifiedAt = models.DateTimeField()
  reportType = models.CharField(max_length=200)
  #data = JSONField(blank=True, help_text="additional fields corresponding to the type in JSON format")

  #SRID 4326 is WGS84 is lon/lat
  #stay with geometries since they support more postgis functions
  #see: http://postgis.refractions.net/documentation/manual-1.5/ch04.html#PostGIS_GeographyVSGeometry
  location = models.PointField(srid=4326, geography=False, blank=True, help_text="String of form POINT(lon, lat)")
