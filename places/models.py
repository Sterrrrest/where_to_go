from django.db import models

r = []
class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    # image = models.ImageField('Каритинка', blank=True, null=True)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('long')
    lat = models.FloatField('lat')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Name', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Картинка', upload_to='media', blank=True, null=True)

    # def count(self):
    #
    #     # list_count = [enumerate(self.place) for i, self in list]
    #         return i
    # place_id = self.place.id
    # r.append(Place.objects.filter(id=place_id))
    # b = []
    # for i, place in enumerate(r):
    #     b.append(i + 1)

    def __str__(self):
        return f'{self.id} {self.place.title}'

