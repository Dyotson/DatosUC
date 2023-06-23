from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Elecciones_FEUC


def index(request):
    return render(request, "main/index.html")


def elecciones_feuc(request):
    elecciones = Elecciones_FEUC.objects
    context = {"elecciones": elecciones}
    return render(request, "main/elecciones_feuc.html", context)
