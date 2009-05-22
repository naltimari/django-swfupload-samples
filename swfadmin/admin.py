from django.contrib import admin
from swfadmin.models import Image, ImageForm

class ImageAdmin(admin.ModelAdmin):
	form = ImageForm

admin.site.register(Image, ImageAdmin)