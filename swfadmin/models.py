from django.db import models
from django import forms

# Create your models here.

class SWFUploadWidget(forms.FileInput):
	class Media:
		css = {
			'all': ('swfupload/css/swfupload.css',)
		}
		js = (
			'swfupload/js/fileprogress.js',
			'swfupload/js/handlers.js',
			'swfupload/js/swfupload.js',
			'swfupload/js/swfupload.queue.js',
			'swfupload/js/swfupload.swfobject.js',
		)

class Image(models.Model):
	title = models.CharField(max_length=200)
	upload = models.ImageField(upload_to='public')
	def __unicode__(self):
		return self.title

class ImageForm(forms.ModelForm):
	upload = forms.FileField(widget=SWFUploadWidget)
	class Meta:
		model = Image