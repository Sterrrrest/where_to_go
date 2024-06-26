import requests
import argparse
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from urllib.request import urlopen

from django.core.files import File
from PIL import Image as Im
from io import BytesIO
from django.core.files.base import ContentFile

from django.core.files.temp import NamedTemporaryFile
from django.core.files.images import ImageFile

from places.models import Place, Image



class Command(BaseCommand):

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        new_place = response.json()
        place = Place.objects.update_or_create(title=new_place['title'],
                                               defaults={
                                                    'short_description': new_place['description_short'],
                                                    'long_description': new_place['description_long'],
                                                    'lng': new_place['coordinates']['lng'],
                                                    'lat': new_place['coordinates']['lat'],
                                                    # 'geo_title': new_place['title'],
                                       })


        for img_num, img in enumerate(new_place['imgs']):
            Image.objects.get_or_create(place=place[0], position=img_num)
            image = Image.objects.get(place=place[0], position=img_num)
            picture = BytesIO(urlopen(img).read())
            image.image.save(f'{img_num}.jpg', picture, save=True)

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            '-u',
            default=False,
            help='URL нового места'
        )

