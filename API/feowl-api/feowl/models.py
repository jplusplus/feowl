from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.auth.hashers import make_password

from tastypie.models import create_api_key
models.signals.post_save.connect(create_api_key, sender=User)


class Contributor(models.Model):
    """Model for a reporter"""

    name = models.CharField('name', max_length=30, unique=True,
        help_text='Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters', blank=True)
    password = models.CharField('password', max_length=128, blank=True)
    email = models.EmailField('e-mail address', blank=True, unique=True)

    credibility = models.DecimalField(max_digits=3, decimal_places=2, default='1.00', blank=True)
    language = models.CharField(max_length=5, default="EN")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __unicode__(self):
        return self.name


class Device(models.Model):
    """Model for the Device"""

    category = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    contributor = models.ForeignKey(Contributor, blank=True, null=True)


class Area(models.Model):
    """Model for the Area"""

    objects = models.GeoManager()

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    overall_population = models.PositiveIntegerField()
    pop_per_sq_km = models.DecimalField(max_digits=8, decimal_places=2)
    geometry = models.PolygonField()

    def kml(self):
        return self.geometry.kml

    def __unicode__(self):
        return self.name


class PowerReport(models.Model):
    """Model for a power cut report"""

    objects = models.GeoManager()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #report_type = models.CharField(max_length=50, null=False, blank=False, choices=(('power', 'Power Cut'), ('other', 'Something else')) )
    #SRID 4326 is WGS84 is lon/lat
    #stay with geometries since they support more postgis functions
    #see: http://postgis.refractions.net/documentation/manual-1.5/ch04.html#PostGIS_GeographyVSGeometry
    quality = models.DecimalField(max_digits=3, decimal_places=2, default='1.00', blank=True)
    duration = models.PositiveIntegerField(null=False, blank=False, help_text="Duration in minutes")
    happened_at = models.DateTimeField(null=False, blank=False, help_text="Datetime preferrably with timezone")
    has_experienced_outage = models.BooleanField(null=False, blank=False, default=True, help_text="Boolean that indicates if user reported a power cut.")

    area = models.ForeignKey(Area, blank=False, null=False)
    contributor = models.ForeignKey(Contributor, blank=True, null=True)
    device = models.ForeignKey(Device, blank=True, null=True)

    deleted = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    location = models.PointField(srid=4326, geography=False, blank=True, null=True, help_text="String in form of POINT(lon, lat)")

    def __unicode__(self):
        if self.contributor:
            return "%s at %s" % (self.contributor, self.happened_at)
        else:
            return "%s" % self.happened_at
