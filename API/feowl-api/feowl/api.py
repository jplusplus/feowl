# this file defines the basic api resources we provide

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.contrib.gis.geos import Point 

from models import HelloFeowl

class HelloFeowlResource(ModelResource):
    class Meta:
        queryset = HelloFeowl.objects.all()
        resource_name = 'hellofeowl'
        
        #danger: this exposes all permissions for anybody, switch to use oauth or api key auth soon
        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authorization = Authorization()
        fields = ['text_1', 'text_2', 'int_1', 'geographic_point_1', 'date_1']

    '''
    alternate post value without hydrate needed: POINT(-101.25 30.751277)
    def hydrate_geographic_point_1(self, bundle):
        #convert POST data into more complex object data
        #assumes the geographic_point_1 data to be in a format of 12.345,67.890 (lat, lon)
        lat = float(bundle.data['geographic_point_1'].split(',')[0])
        lon = float(bundle.data['geographic_point_1'].split(',')[1])
        point = Point(lon, lat, srid=4326)
        bundle.data['geographic_point_1'] = point
        return bundle.data
    '''