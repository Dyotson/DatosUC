from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Elecciones_FEUC, Consejo_FEUC, Votaciones_FEUC


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
    return render(request, "main/elecciones/elecciones_feuc.html", context)


def votaciones_feuc(request):
    anos = Consejo_FEUC.objects.order_by("-ano").values_list("ano", flat=True)
    votaciones_feuc = Votaciones_FEUC.objects.all()
    context = {
        "votaciones": votaciones_feuc,
        "anos": anos,
    }
    return render(request, "main/votaciones/votaciones_feuc.html", context)


def colaboradores(request):
    return render(request, "main/colaboradores.html")


def como_funciona(request):
    return render(request, "main/como_funciona.html")
