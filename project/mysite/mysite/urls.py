from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Result/$', 'mysite.views.Result'),
    url(r'^viewCSV/$', 'mysite.views.viewCSV'),
    url(r'^viewTotal/$', 'mysite.views.viewTotal'),
    url(r'^JavaRead/$', 'mysite.views.JavaRead'),
    url(r'^eXist/$', 'mysite.views.eXist'),
    url(r'^index/$', 'mysite.views.index'),
    url(r'^main/$', 'mysite.views.main'),
    url(r'^admin/', include(admin.site.urls)),

)
