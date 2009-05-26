from django.contrib import admin
from swfadmin.models import Image, ImageForm

class ImageAdmin(admin.ModelAdmin):
	form = ImageForm
	fieldsets = (
		( None, {'fields': ('title',)}),
		( 'Uploads', {'fields': ('upload',)}),
	)

admin.site.register(Image, ImageAdmin)