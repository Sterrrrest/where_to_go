from django.contrib import admin
from places.models import Place, Image


class Imageinline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [Imageinline]
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place',)

# Register your models here.
