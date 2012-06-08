from django.contrib.gis import admin
from models import Report, Area, Device

admin.site.register(Report, admin.OSMGeoAdmin)
admin.site.register(Area, admin.OSMGeoAdmin)
admin.site.register(Device)
