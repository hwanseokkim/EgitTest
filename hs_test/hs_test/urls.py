from django.conf.urls import patterns, include, url
from test.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^user/(.+)/$', user_page),
    # Examples:
    # url(r'^$', 'hs_test.views.home', name='home'),
    # url(r'^hs_test/', include('hs_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
