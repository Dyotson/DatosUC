from django.contrib import admin
from .models import Elecciones_FEUC, Consejo_FEUC, Votaciones_FEUC


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


@admin.register(Consejo_FEUC)
class Consejo_FEUCAdmin(admin.ModelAdmin):
    list_display = ["ano"]


@admin.register(Votaciones_FEUC)
class Votaciones_FEUCAdmin(admin.ModelAdmin):
    list_display = ["consejo", "votacion", "votos"]


# Register your models here.
