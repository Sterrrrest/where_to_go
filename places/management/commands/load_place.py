import requests
import time

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
# from urllib.error import HTTPError

from places.models import Place, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            new_place = response.json()
            place, created = Place.objects.update_or_create(title=new_place['title'],
                                                   defaults={
                                                        'short_description': new_place['description_short'],
                                                        'long_description': new_place['description_long'],
                                                        'lng': new_place['coordinates']['lng'],
                                                        'lat': new_place['coordinates']['lat'],
                                           })

            for img_num, img in enumerate(new_place['imgs']):
                try:
                    pic_response = requests.get(img)
                    pic_response.raise_for_status()
                    image = ContentFile(pic_response.content, name=f'{img_num}.jpg')
                    Image.objects.create(place=place, image=image, position=img_num)
                except requests.exceptions.HTTPError:
                    print('HTTPError')
                except requests.exceptions.ConnectionError:
                    print('ConnectionError')
        except requests.exceptions.HTTPError:
            print('HTTPError')
        except requests.exceptions.ConnectionError:
            print('ConnectionError')

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            '-u',
            help='URL нового места'
        )

