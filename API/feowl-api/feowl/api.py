# this file defines the basic api resources we provide

from tastypie import fields
from tastypie.resources import Resource, ModelResource, ALL
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.validation import FormValidation

from django.conf.urls.defaults import url

from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from decimal import *

from models import PowerReport, Device, Contributor, Area
from forms import PowerReportForm, DeviceForm, ContributorForm, AreaForm

from django.forms.models import ModelChoiceField


class ModelFormValidation(FormValidation):
    """
    Override tastypie's standard ``FormValidation`` since this does not care
    about URI to PK conversion for ``ToOneField`` or ``ToManyField``.
    """

    def uri_to_pk(self, uri):
        """
        Returns the integer PK part of a URI.

        Assumes ``/api/v1/resource/123/`` format. If conversion fails, this just
        returns the URI unmodified.

        Also handles lists of URIs
        """

        if uri is None:
            return None

        # convert everything to lists
        multiple = not isinstance(uri, basestring)
        uris = uri if multiple else [uri]

        # handle all passed URIs
        converted = []
        for one_uri in uris:
            try:
                # hopefully /api/v1/<resource_name>/<pk>/
                converted.append(int(one_uri.split('/')[-2]))
            except (IndexError, ValueError):
                raise ValueError(
                    "URI %s could not be converted to PK integer." % one_uri)

        # convert back to original format
        return converted if multiple else converted[0]

    def is_valid(self, bundle, request=None):
        data = bundle.data
        # Ensure we get a bound Form, regardless of the state of the bundle.
        if data is None:
            data = {}
        # copy data, so we don't modify the bundle
        data = data.copy()

        # convert URIs to PK integers for all relation fields
        relation_fields = [name for name, field in
                           self.form_class.base_fields.items()
                           if issubclass(field.__class__, ModelChoiceField)]

        for field in relation_fields:
            if field in data:
                data[field] = self.uri_to_pk(data[field])

        # validate and return messages on error
        form = self.form_class(data)
        if form.is_valid():
            return {}
        return form.errors


class ContributorResource(ModelResource):
    class Meta:
        queryset = Contributor.objects.all()
        resource_name = 'contributors'

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        validation = ModelFormValidation(form_class=ContributorForm)

        fields = ['id', 'email', 'password', 'name', 'language']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "credibility": ALL,
            "language": ALL,
            "name": ALL,
            "email": ALL,
        }

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\d+?)/check_password/$" % self._meta.resource_name, self.wrap_view('check_password'), name="api_check_password"),
        ]

    def check_password(self, request, **kwargs):
        '''
        method to verify a raw password against the saved encrypted one (only use through SSL!)
        '''
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        try:
            obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")

        valid = check_password(request.GET.get('password'), obj.password)

        self.log_throttled_access(request)

        bundle = self.build_bundle(obj=obj, request=request)
        bundle = self.full_dehydrate(bundle)
        bundle = self.alter_detail_data_to_serialize(request, bundle)

        #add out result
        bundle.data['password_valid'] = valid
        bundle.data['password'] = settings.DUMMY_PASSWORD
        return self.create_response(request, bundle)

    def hydrate_password(self, bundle):
        """Turn a passed in password into a hash so it is not saved raw."""
        bundle.data['password'] = make_password(bundle.data.get('password'))
        return bundle

    def dehydrate_password(self, bundle):
        return settings.DUMMY_PASSWORD


class DeviceResource(ModelResource):
    contributor = fields.ForeignKey(ContributorResource, 'contributor', null=True)

    class Meta:
        queryset = Device.objects.all()
        resource_name = 'devices'

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        validation = ModelFormValidation(form_class=DeviceForm)

        fields = ['category', 'phone_number', 'contributor']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']

        filtering = {
            'contributor': ALL  # ALL_WITH_RELATIONS ?
        }


class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        resource_name = 'areas'

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        validation = ModelFormValidation(form_class=AreaForm)

        fields = ['name', 'city', 'country', 'pop_per_sq_km', 'overall_population']

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        #allow filtering on the collection to do things like /api/v1/areas/?name_ilike=douala
        filtering = {
            'name': ALL,
            'country': ALL,
            'overall_population': ALL
        }


class PowerReportResource(ModelResource):
    area = fields.ForeignKey(AreaResource, 'area', null=False)
    contributor = fields.ForeignKey(ContributorResource, 'contributor', null=True)
    device = fields.ForeignKey(DeviceResource, 'device', null=True)

    class Meta:
        queryset = PowerReport.objects.all()
        resource_name = 'reports'

        #see: http://www.infoq.com/news/2010/01/rest-api-authentication-schemes
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        validation = ModelFormValidation(form_class=PowerReportForm)

        #whitelist of fields to be public
        fields = ['quality', 'duration', 'happened_at', 'has_experienced_outage', 'location', 'area', 'contributor', 'device']

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']

        filtering = {
            'quality': ALL,
            'duration': ALL,
            'happened_at': ALL,
        }


class GenericResponseObject(object):
    '''
    generic object to represent dict values as attributes (returned as tastypie response object)
    '''
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
        object_class = GenericResponseObject
        include_resource_uri = False

        list_allowed_methods = ['get']
        detail_allowed_methods = []

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

        #TODO: we need a custom validation class for this as there is no model...

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
            result.append(GenericResponseObject({'area': area, 'avg_duration': avg_duration, 'affected_population': aff_population}))
        return result
