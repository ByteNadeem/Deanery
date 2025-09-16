from django.shortcuts import render
from django.conf import settings

# Create your views here.


def map_home(request):
    return render(request, 'map/map_home.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })
