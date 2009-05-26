from django.db import models
from django import forms
from django.utils.safestring import mark_safe

# Create your models here.

class Album(models.Model):
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class Image(models.Model):
	upload = models.ImageField(upload_to='media', blank=True)
	title = models.CharField(max_length=200, blank=True)
	album = models.ForeignKey(Album)
	def __unicode__(self):
		return self.upload.name

swfinit = """
<script type="text/javascript">
var swfu;
window.onload = function() {
	var settings = {
		flash_url : "/media/swfupload/swf/swfupload.swf",
		upload_url: "/swfupload/upload.php",
		post_params: {"PHPSESSID" : "%s"},
		file_size_limit : "1 MB",
		file_types : "*.jpg;*.jpeg",
		file_types_description : "JPEG Files",
		file_upload_limit : 100,
		file_queue_limit : 0,
		custom_settings : {
			progressTarget : "fsUploadProgress",
			cancelButtonId : "btnCancel"
		},
		debug: false,

		// Button settings
		button_width: "114",
		button_height: "24",
		button_placeholder_id: "spanButtonPlaceHolder",
		button_window_mode: SWFUpload.WINDOW_MODE.TRANSPARENT,
		
		// The event handler functions are defined in handlers.js
		file_queued_handler : fileQueued,
		file_queue_error_handler : fileQueueError,
		file_dialog_complete_handler : fileDialogComplete,
		upload_start_handler : uploadStart,
		upload_progress_handler : uploadProgress,
		upload_error_handler : uploadError,
		upload_success_handler : uploadSuccess,
		upload_complete_handler : uploadComplete,
		queue_complete_handler : queueComplete	// Queue plugin event
	};

	swfu = new SWFUpload(settings);
 };
</script>
<div style="margin-left: 105px">
<div class="fieldset flash" id="fsUploadProgress">
	<span class="legend">Arquivos a transmitir</span>
</div>
<span id="spanButtonPlaceHolder"></span>
<input type="button" value="Escolher arquivos" />
<input id="btnCancel" type="button" value="Abortar" onclick="swfu.cancelQueue();" disabled="disabled" />
</div>
"""

# Create your models here.

class ImageThumbWidget(forms.HiddenInput):
	def render(self, name, value, attrs=None):
		hidden = super(ImageThumbWidget, self).render(name, value, attrs)
		return mark_safe(u'%s<img src="/%s" width="70" height="70">' % (hidden, value))

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
	def render(self, name, value, attrs=None):
		return mark_safe(u''.join(swfinit % attrs))

class AlbumForm(forms.ModelForm):
	upload = forms.CharField(
		widget=SWFUploadWidget(
			attrs={
				'caption': 'teste',
				'session_id': 'teste',
			}
		),
		required=False,
	)
	class Meta:
		model = Album
		
class ImageForm(forms.ModelForm):
	upload = forms.CharField(
		widget=ImageThumbWidget
	)
	class Meta:
		model = Image