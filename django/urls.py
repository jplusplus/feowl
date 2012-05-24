from django.conf.urls.defaults import patterns, include, url
# import the view from helloapp
from helloapp.views import hello_view
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from feowl.api import HelloFeowlResource

admin.autodiscover()

hello_feowl = HelloFeowlResource()

urlpatterns = patterns('',
    url(r'^$', view=hello_view, name='hello_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(hello_feowl.urls)),
)
