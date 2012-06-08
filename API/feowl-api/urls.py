from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from tastypie.api import Api
from feowl.api import ReportsResource

admin.autodiscover()

#bind all resources together for our API
v1_api = Api(api_name='v1')
v1_api.register(ReportsResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^test/', TemplateView.as_view(template_name="test.html")),
)
