from django.conf.urls import patterns, include, url
from blogsource.feeds import LatestEntriesFeed

urlpatterns = patterns('blogsource',
    (r'^$', 'views.index'),
    (r'^view/(?P<slug>[^\.]+).html', 'views.view_post'),
    (r'^category/(?P<slug>[^\.]+).html', 'views.view_category'),
    (r'^latest/rss/$', LatestEntriesFeed()),
)
