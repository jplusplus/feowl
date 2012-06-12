# this file defines the basic api resources we provide

from tastypie import fields
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
# from django.contrib.gis.geos import Point
from models import Report, Device, UserProfile, Area


class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'devices'

        authorization = Authorization()

        fields = ['category', 'phone_number']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']


class UserResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'users'

        authorization = Authorization()

        fields = ['username', 'credibility', 'language']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            'username':ALL
        }
        
class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        resource_name = 'areas'

        fields = ['name', 'city', 'country', 'pop_per_sq_km']

        list_allowed_methods = ['get', 'post']
        
        #allow filtering on the collection to do things like /api/v1/areas/?name_ilike=douala
        filtering = {
            'name': ALL
        }
        

class ReportResource(ModelResource):
    area = fields.ForeignKey(AreaResource, 'area', null=False)
    
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'reports'
        
        #danger: this exposes all permissions for anybody, switch to use api key auth soon
        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authorization = Authorization()

        #whitelist of fields to be public
        fields = ['report_type', 'location', 'area', 'user', 'device']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']

        filtering = {
            'report_type': ALL
        }