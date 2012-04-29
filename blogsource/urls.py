from django.conf.urls import patterns, include, url

urlpatterns = patterns('blogsource',
    (r'^$', 'views.index'),
    (r'^view/(?P<slug>[^\.]+).html', 'views.view_post'),
    (r'^category/(?P<slug>[^\.]+).html', 'views.view_category'),
)
