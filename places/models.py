from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Каритинка', blank=True, null=True)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('long')
    lat = models.FloatField('lat')

    def __str__(self):
        return self.title
# Create your models here.
