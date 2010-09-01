from django.conf.urls.defaults import *
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os
def serve_html(request, path):
	return render_to_response(os.path.join(settings.MEDIA_ROOT, path, 'index.php'))

def upload(request):
	if request.method == 'POST':
		if request.FILES:
			print request.POST
			return HttpResponse()
	raise Http404

urlpatterns = patterns('django.views',
	(r'^.+/upload.php', upload),
	(r'^(?P<path>.+)/index.php', serve_html),
	(r'^(?P<path>.+)$', 'static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^$', 'generic.simple.direct_to_template', {'template': 'index.htm'}),
)
