from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase
from adminsortable2.admin import SortableTabularInline




class Imageinline(SortableTabularInline):
    model = Image
    fields = ('image', 'preview_img', 'position',)
    readonly_fields = ('preview_img',)

    def preview_img(self, obj):
        return format_html('<img src="{url}" style="max-height: 200px;">'.format(
            url=obj.image.url,
        )
    )

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):

    inlines = [Imageinline]
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place',)

# Register your models here.
