
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("venue/", views.venue, name='venue'),
    path("privacy/", views.privacy, name='privacy'),
    path("online/", views.online, name='online'),
    path("contact/", views.contact, name='contact'),  
]
