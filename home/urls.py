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
    path('churches/', views.churches, name='churches'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutPage.as_view(), name='about'),
    # Events urls here
    path('events/', views.EventListView.as_view(), name='events'),
    path(
        'events/<int:pk>/',
        views.EventDetailView.as_view(),
        name='event_detail'
    ),
    path('events/new/', views.EventCreateView.as_view(), name='event_new'),
    path(
        'events/<int:pk>/edit/',
        views.EventUpdateView.as_view(),
        name='event_edit'
    ),
    path(
        'events/<int:pk>/delete/',
        views.EventDeleteView.as_view(),
        name='event_delete'
    ),
    path('events/<int:pk>/like/', views.event_like, name='event_like'),
]
