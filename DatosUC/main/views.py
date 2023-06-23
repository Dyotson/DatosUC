from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Elecciones_FEUC


def index(request):
    return render(request, "main/index.html")


def elecciones_feuc(request):
    anos = (
        Elecciones_FEUC.objects.order_by("-ano")
        .values_list("ano", flat=True)
        .distinct()
    )
    elecciones = Elecciones_FEUC.objects.all()
    context = {
        "elecciones": elecciones,
        "anos": anos,
    }
    return render(request, "main/elecciones_feuc.html", context)
