
# ============
from tastypie.resources import ModelResource
from models import HelloFeowl


class EntryResource(ModelResource):
    class Meta:
        queryset = HelloFeowl.objects.all()
        resource_name = 'entry'
