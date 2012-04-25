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
#    (r"^add_comment/(?P<slug>[^\.]+)/$", "blogsource.views.add_comment"),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
