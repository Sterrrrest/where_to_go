from django.contrib import admin
from places.models import Place, Image
from django.utils.html import mark_safe, format_html


class Imageinline(admin.TabularInline):
    model = Image
    fields = ('image', 'preview_img', 'position',)
    readonly_fields = ('preview_img',)

    def preview_img(self, obj):
        return format_html('<img src="{url}" style="max-height: 200px;">'.format(
            url=obj.image.url,
        )
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [Imageinline]
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place',)

# Register your models here.
