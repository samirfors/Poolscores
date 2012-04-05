from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index/$', 'scores.views.index'),
	url(r'^tournament/(?P<t_id>\d+)/$', 'scores.views.detail'),
	url(r'^tournament/create/$', 'scores.views.create'),
	url(r'^tournament/fixture/(?P<f_id>\d+)/$', 'scores.views.fixture'),
    url(r'^admin/', include(admin.site.urls)),
)
