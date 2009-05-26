from django.contrib import admin
from swfadmin.models import Album, Image, AlbumForm, ImageForm

class ImageInlineAdmin(admin.TabularInline):
	form = ImageForm
	model = Image
	extra = 0

class AlbumAdmin(admin.ModelAdmin):
	form = AlbumForm
	fieldsets = (
		( None, {'fields': ('title',)}),
		( 'Uploads', {'fields': ('upload',)}),
	)
	inlines = [ImageInlineAdmin]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image)