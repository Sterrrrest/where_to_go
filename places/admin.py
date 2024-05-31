from django.contrib import admin
from places.models import Place, Image


admin.site.register(Place)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place',)

# Register your models here.
