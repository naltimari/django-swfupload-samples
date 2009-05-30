from django.contrib import admin
from swfadmin.models import Album, Image, AlbumForm, ImageForm

class ImageInlineAdmin(admin.TabularInline):
	template = 'admin/edit_inline/tabular_sortable.html'
	form = ImageForm
	model = Image
	extra = 0

class AlbumAdmin(admin.ModelAdmin):
	form = AlbumForm
	fieldsets = (
		( None, {'fields': ('title',)}),
		( 'Uploads', {'fields': ('upload',)}),
	)
	list_display = ('title','itens')
	inlines = [ImageInlineAdmin]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image)