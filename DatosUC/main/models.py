from django.db import models

# Create your models here.


class Elecciones_FEUC(models.Model):
    ano = models.IntegerField()
    vuelta = models.IntegerField()
    quorum = models.FloatField()
    numero_votantes = models.IntegerField()
    porcentaje_mg = models.FloatField()
    votos_mg = models.IntegerField()
    porcentaje_sdd = models.FloatField()
    votos_sdd = models.IntegerField()
    porcentaje_avnzr = models.FloatField()
    votos_avnzr = models.IntegerField()
    porcentaje_nau = models.FloatField()
    votos_nau = models.IntegerField()
    porcentaje_surgencia = models.FloatField()
    votos_surgencia = models.IntegerField()
    porcentaje_nulo = models.FloatField()
    votos_nulo = models.IntegerField()
    porcentaje_blanco = models.FloatField()
    votos_blanco = models.IntegerField()

    class Meta:
        ordering = ("ano", "vuelta")


class Consejo_FEUC(models.Model):
    ano = models.IntegerField()


class Votaciones_FEUC(models.Model):
    votacion = models.CharField(max_length=100)
    apruebo = models.IntegerField()
    rechazo = models.IntegerField()
    abstencion = models.IntegerField()
    consejo = models.ForeignKey(Consejo_FEUC, on_delete=models.CASCADE)
