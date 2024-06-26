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

from PIL import Image as Im


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
            pic_response = requests.get(img).content
            image = ContentFile(pic_response, name=f'{img_num}.jpg')
            Image.objects.create(place=place[0], image=image, position=img_num)


    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            '-u',
            default=False,
            help='URL нового места'
        )

