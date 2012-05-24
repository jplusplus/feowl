from tastypie.resources import ModelResource
from models import HelloFeowl


class HelloFeowlResource(ModelResource):
    class Meta:
        queryset = HelloFeowl.objects.all()
        resource_name = 'HelloFeowl'
