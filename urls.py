from django.conf.urls.defaults import *
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
def php2html(request, path, page):
	return render_to_response(os.path.join(settings.MEDIA_ROOT + '/demos', path) + '\\%s.php' % page)

def handle_uploaded_file(f):
    destination = open(settings.MEDIA_ROOT + '/media/' + f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def upload(request):
	if request.method == 'POST':
		if request.FILES:
			for f in request.FILES:
				handle_uploaded_file(request.FILES[f])
		return HttpResponse()
	raise Http404

urlpatterns = patterns('django.views',
	(r'^admin/(.*)', admin.site.root),
	(r'^media/(?P<path>.+)$', 'static.serve', {'document_root': settings.MEDIA_ROOT +'/media'}),
	(r'^.+/upload.php', upload),
	(r'^(?P<path>.+)/(?P<page>.+).php', php2html),
	(r'^(?P<path>.+)$', 'static.serve', {'document_root': settings.MEDIA_ROOT +'/demos'}),
	(r'^$', 'generic.simple.direct_to_template', {'template': 'index.htm'}),
)
