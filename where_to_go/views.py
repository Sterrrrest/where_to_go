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
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat]
                    },
                    "properties": {
                        "title": place.geo_title,
                        "placeId": place.placeId,
                        "detailsUrl": reverse('places', kwargs={'id': place.id})
                    }
                },)

    value = {
        "type": "FeatureCollection",
        "features": feature
    }
    data = {'value': value}
    return render(request, 'index.html', context=data)


def get_place(request, id):
    place = get_object_or_404(Place, id=id)
    images = Image.objects.filter(place_id=id)

    point = {
        "title": place.title,
        "imgs": [pic.image.url for pic in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(point, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
