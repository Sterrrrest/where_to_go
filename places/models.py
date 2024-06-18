from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Длинное описание')
    lng = models.FloatField(verbose_name='Длина')
    lat = models.FloatField(verbose_name='Широта')

    geo_title = models.CharField('Название на карте', max_length=50, blank=True)
    placeId = models.CharField('ID', max_length=50, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Название', related_name='place_images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Картинка', upload_to='media', blank=True, null=True)
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
