from . import views
from django.urls import path
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path('signup/', views.newsletter_signup, name='newsletter_signup'),
    path(
        'confirm/<uuid:token>/',
        views.newsletter_confirm,
        name='newsletter_confirm'
    ),
    path(
        'unsubscribe/<uuid:token>/',
        views.newsletter_unsubscribe,
        name='newsletter_unsubscribe'
    ),
    path('churches/', views.ChurchListView.as_view(), name='church_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutPage.as_view(), name='about'),
]
