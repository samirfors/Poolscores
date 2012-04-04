from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^scores/$', 'scores.views.index'),
	url(r'^scores/(?P<t_id>\d+)/$', 'scores.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
