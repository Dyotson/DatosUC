from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("datos/elecciones_feuc", views.elecciones_feuc, name="elecciones_feuc"),
    path("datos/votaciones_feuc", views.votaciones_feuc, name="votaciones_feuc"),
]
