from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^(?P<path>(?:css|images|js|swf|versioned).*)',
     'django.views.static.serve',
     {'document_root': '/home/vagrant/src/miro-community/static/'}),
    (r'^uploadtemplate/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': '/home/vagrant/src/localtv-themes/'}),
    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': '/home/vagrant/media'}),
    (r'', include('localtv.urls')),

                       )
