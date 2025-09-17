from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_home, name='map_home'),
]
