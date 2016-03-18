from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import app.views


from django.conf.urls import patterns, include, url
from app.app.api.api import LocationResource
from app.app.views import location

location_resource = LocationResource()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^db', app.views.db, name='db'),
 	url(r'^api/', include(location_resource.urls)),
	url(r'^v0/locations/$',location.locationSearch),
   
]
