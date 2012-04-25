from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blogsource.views.index'),
    url(r'^blogsource/view/(?P<slug>[^\.]+).html', 
        'blogsource.views.view_post',
        name='view_blog_post'),
    url(r'^blogsource/category/(?P<slug>[^\.]+).html', 
        'blogsource.views.view_category', 
        name='view_blog_category'),
    url(r'^admin/', include(admin.site.urls)),
)
