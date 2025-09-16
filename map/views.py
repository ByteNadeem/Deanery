from django.shortcuts import render

# Create your views here.


def map_home(request):
    return render(request, 'map/map_home.html')
