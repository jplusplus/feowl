# this file defines the basic api resources we provide

from tastypie import fields
from tastypie.resources import Resource, ModelResource, ALL
from tastypie.authorization import DjangoAuthorization
# from tastypie.authentication import ApiKeyAuthentication
from tastypie_auth import ConfigurableApiKeyAuthentication
# from django.contrib.gis.geos import Point
from models import PowerReport, Device, UserProfile, Area

from django.conf.urls.defaults import url
from django.contrib.auth.models import User
from django.db import models
from tastypie.models import create_api_key

from django.db import IntegrityError
from tastypie.exceptions import BadRequest

models.signals.post_save.connect(create_api_key, sender=User)

from decimal import *


class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'devices'

        authentication = ConfigurableApiKeyAuthentication(username_param='user_name')
        authorization = DjangoAuthorization()

        fields = ['category', 'phone_number']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']


class UserProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'userprofiles'
        include_resource_uri = False
        include_absolute_url = False

        authentication = ConfigurableApiKeyAuthentication(username_param='user_name')
        authorization = DjangoAuthorization()

        fields = ['credibility', 'language']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "credibility": ALL,
            "language": ALL,
        }


class UserResource(ModelResource):
    profile = fields.ToOneField(UserProfileResource, 'get_profile', full=True)

    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()

        authentication = ConfigurableApiKeyAuthentication(username_param='user_name')
        authorization = DjangoAuthorization()

        fields = ['email', 'password', 'username']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "username": ALL,
            "email": ALL,
        }

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            bundle = super(UserResource, self).obj_create(bundle, request, **kwargs)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.save()
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle


class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        resource_name = 'areas'

        authentication = ConfigurableApiKeyAuthentication(username_param='user_name')
        authorization = DjangoAuthorization()

        fields = ['name', 'city', 'country', 'pop_per_sq_km']

        list_allowed_methods = ['get']
        # TODO: Why we need a put if we're creating a report with a area with {"pk":1}
        detail_allowed_methods = ['put', 'get']

        #allow filtering on the collection to do things like /api/v1/areas/?name_ilike=douala
        filtering = {
            'name': ALL
        }


class PowerReportResource(ModelResource):
    area = fields.ForeignKey(AreaResource, 'area', null=False)

    class Meta:
        queryset = PowerReport.objects.all()
        resource_name = 'reports'

        #danger: this exposes all permissions for anybody, switch to use api key auth soon
        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authentication = ConfigurableApiKeyAuthentication(username_param='user_name')
        authorization = DjangoAuthorization()

        #whitelist of fields to be public
        fields = ['quality', 'duration', 'happened_at', 'has_experienced_outage', 'location', 'area', 'user', 'device']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']

        filtering = {
            'quality': ALL,
            'duration': ALL,
            'happened_at': ALL,
        }


class AggregationObject(object):
    #generic object to represent dict values as attributes (returned as tastypie response object)
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class PowerReportAggregatedResource(Resource):
    area = fields.ForeignKey(AreaResource, 'area', help_text="The area the data is about")
    avg_duration = fields.DecimalField('avg_duration', help_text="Average duration of a power cut over all power cuts")
    affected_population = fields.DecimalField('affected_population', help_text="An approximate percentage of the people in the area that are affected by power cuts.")

    class Meta:
        resource_name = 'aggregation'
        object_class = AggregationObject
        include_resource_uri = False

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = []

    def base_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/reports/$" % self._meta.resource_name, self.wrap_view('dispatch_list_aggregated'), name="api_dispatch_list_aggregated"),
            url(r"^(?P<resource_name>%s)/reports/schema/$" % self._meta.resource_name, self.wrap_view('get_schema'), name='api_get_schema')
        ]

    def dispatch_list_aggregated(self, request, resource_name, **kwargs):
        return self.dispatch_list(request, **kwargs)

#    def obj_get(self, request=None, **kwargs):
#        #tastypie method override
#        return PowerReportResource().obj_get(request, **kwargs)

    def obj_get_list(self, request=None, **kwargs):
        #tastypie method override
        obj_list = PowerReportResource().obj_get_list(request, **kwargs)
        return self.aggregate_reports(obj_list)

    def aggregate_reports(self, filtered_objects):
        result = []

        #get all areas
        areas = Area.objects.all()

        getcontext().prec = 2

        for area in areas:
            #get reports in each area
            area_reports = filtered_objects.filter(area=area.id)
            actual_powercut_reports = filtered_objects.filter(area=area.id, has_experienced_outage=True)

            #average power cut duration
            avg_duration = 0
            if len(actual_powercut_reports):
                for r in actual_powercut_reports:
                    avg_duration += r.duration
                avg_duration = Decimal(avg_duration) / Decimal(len(actual_powercut_reports))

            #affected population percentage
            aff_population = 0
            if len(area_reports) and len(actual_powercut_reports):
                aff_population = Decimal(len(actual_powercut_reports)) / Decimal(len(area_reports))

            #create aggregate object
            result.append(AggregationObject({'area': area, 'avg_duration': avg_duration, 'affected_population': aff_population}))
        return result
