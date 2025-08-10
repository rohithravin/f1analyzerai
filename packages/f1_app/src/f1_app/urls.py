from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Index page
    path("drivers/", views.drivers, name="drivers"),
    path("constructors/", views.constructors, name="constructors"),
    path("race/", views.race, name="race"),
]
