from django.contrib import admin
from .models import Elecciones_FEUC


@admin.register(Elecciones_FEUC)
class Elecciones_FEUCAdmin(admin.ModelAdmin):
    list_display = [
        "ano",
        "vuelta",
        "quorum",
        "numero_votantes",
        "porcentaje_mg",
        "votos_mg",
        "porcentaje_sdd",
        "votos_sdd",
        "porcentaje_avnzr",
        "votos_avnzr",
        "porcentaje_nau",
        "votos_nau",
        "porcentaje_surgencia",
        "votos_surgencia",
        "porcentaje_nulo",
        "votos_nulo",
        "porcentaje_blanco",
        "votos_blanco",
    ]


# Register your models here.
