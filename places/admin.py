from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableTabularInline


height = 200
width = 300

class Imageinline(SortableTabularInline):
    model = Image
    fields = ('image', 'preview_img', 'position',)
    readonly_fields = ('preview_img',)

    def preview_img(self, obj):
        return format_html("<img src={} style='max-height: {}px; max-width: {}px;'>",
                           mark_safe(obj.image.url), height, width)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):

    inlines = [Imageinline]
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
