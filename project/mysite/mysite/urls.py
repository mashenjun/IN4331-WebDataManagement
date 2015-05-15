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
    url(r'^Xquerytest/$', 'mysite.views.Xquerytest'),
    url(r'^Xquerytest/summary/([a-zA-Z\s\-]+)/$', 'mysite.views.summary'),
    url(r'^sha_index/$', 'mysite.views.sha_index'),
    url(r'^sha_poetry/([\d]+)/$', 'mysite.views.sha_poetry'),
    url(r'^sha_npoetry/([\d]+)/$', 'mysite.views.sha_npoetry'),
    url(r'^sha_poetry_list/([a-zA-Z\d\@]+)/$', 'mysite.views.sha_poetry_list'),
    url(r'^sha_npoetry_list/([a-zA-Z\d\@]+)/$', 'mysite.views.sha_npoetry_list'),
    url(r'^music_index/$', 'mysite.views.music_index'),
    url(r'^music_PDF/([a-zA-Z\d_\.]+)/$', 'mysite.views.music_PDF'),
    url(r'^xslttest/$', 'mysite.views.xslttest'),
    url(r'^pdfreturn/$', 'mysite.views.pdfreturn'),
    url(r'^uploadfile/$','mysite.test.uploadfile'),
    url(r'^upload_file/([a-zA-Z\d_\.]+)/$','mysite.test.upload_file'),
    url(r'^index/$', 'mysite.views.index'),
    url(r'^main/$', 'mysite.views.main'),
    url(r'^create_midi/$', 'mysite.views.create_midi'),
    url(r'^sendrequest/$','mysite.views.sendrequest'),
    url(r'^admin/', include(admin.site.urls)),

)
