# this file defines the basic api resources we provide

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.contrib.gis.geos import Point 
from models import Report

class ReportsResource(ModelResource):
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'reports'
        
        #danger: this exposes all permissions for anybody, switch to use oauth or api key auth soon
        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authorization = Authorization()
        
        #whitelist of fields to be public
        fields = ['createdAt', 'modifiedAt', 'reportType', 'location']