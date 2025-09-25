from . import views
from django.urls import path

urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
    path('signup/', views.newsletter_signup, name='newsletter_signup'),
    path('confirm/<uuid:token>/', views.newsletter_confirm, name='newsletter_confirm'),
    path('unsubscribe/<uuid:token>/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
]