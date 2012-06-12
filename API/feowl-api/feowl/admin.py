from django.contrib.gis import admin
from models import PowerReport, Area, Device

from tastypie.admin import ApiKeyInline
from tastypie.models import ApiAccess, ApiKey
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(PowerReport, admin.OSMGeoAdmin)
admin.site.register(Area, admin.OSMGeoAdmin)
admin.site.register(Device)

admin.site.register(ApiKey)
admin.site.register(ApiAccess)

class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]

admin.site.unregister(User)
admin.site.register(User,UserModelAdmin)