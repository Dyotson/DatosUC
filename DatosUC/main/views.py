from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def elecciones_feuc(request):
    return render(request, "main/elecciones_feuc.html")
