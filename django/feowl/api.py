
# ============
from tastypie.resources import ModelResource
from models import HelloWorld


class EntryResource(ModelResource):
    class Meta:
        queryset = HelloWorld.objects.all()
        resource_name = 'entry'
