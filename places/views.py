from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    feature = []
    for place in places:
        feature.append({
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.lng, place.lat]
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.id,
                        'detailsUrl': reverse('places', kwargs={'id': place.id})
                    }
                },)

    place_data = {
        'type': 'FeatureCollection',
        'features': feature
    }

    return render(request, 'index.html', context={'place_data': place_data})


def get_place(request, id):

    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)

    point = {
        'title': place.title,
        'imgs': [pic.image.url for pic in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(point, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
