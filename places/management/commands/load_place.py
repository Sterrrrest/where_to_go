import requests
import time

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
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
                pic_response = requests.get(img)
                pic_response.raise_for_status()
                image = ContentFile(pic_response.content, name=f'{img_num}.jpg')
                Image.objects.create(place=place[0], image=image, position=img_num)
        except requests.exceptions.HTTPError:
            print('HTTPError')
        except requests.exceptions.ConnectionError:
            time.sleep(30)
            
    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            '-u',
            default=False,
            help='URL нового места'
        )

