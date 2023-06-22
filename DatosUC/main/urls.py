from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("datos/elecciones_feuc", views.elecciones_feuc, name="elecciones_feuc"),
]
