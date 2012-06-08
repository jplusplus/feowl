# this file defines the basic api resources we provide

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
# from django.contrib.gis.geos import Point
from models import Report, Device, UserProfile, Area


class ReportsResource(ModelResource):
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'reports'

        #danger: this exposes all permissions for anybody, switch to use oauth or api key auth soon
        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authorization = Authorization()

        #whitelist of fields to be public
        fields = ['report_type', 'location', 'area', 'user', 'device']


class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'devices'

        authorization = Authorization()

        fields = ['categorie', 'phone_number']


class  UserResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'users'

        authorization = Authorization()

        fields = ['username', 'credibility', 'language']


class  AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        resource_name = 'areas'

        authorization = Authorization()

        fields = ['name', 'city', 'country', 'pop_per_sq_km']
