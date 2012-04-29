from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
import blogsource.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/blogsource/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blogsource/', include('blogsource.urls')),
)
