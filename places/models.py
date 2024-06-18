from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=150)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField(verbose_name='Длина')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Название', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Картинка', upload_to='media')
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
