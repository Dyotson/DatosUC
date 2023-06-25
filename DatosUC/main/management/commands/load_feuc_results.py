from csv import DictReader
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

# Import the model
from main.models import Elecciones_FEUC


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from csv of FEUC elections into our database"

    def add_arguments(self, parser):
        parser.add_argument(
            "path", type=str, help="Indicates the path of the file to be imported"
        )

    def handle(self, *args, **options):
        # Code to load the data into database
        print("Importing data from", options["path"])
        for row in DictReader(open(options["path"], encoding="utf-8"), delimiter=";"):
            print("Importing", row["ano"], "vuelta", row["vuelta"], "elections")
            eleccion = Elecciones_FEUC(
                ano=row["ano"],
                vuelta=row["vuelta"],
                quorum=row["quorum"],
                numero_votantes=row["numero_votantes"],
                porcentaje_mg=row["porcentaje_mg"],
                votos_mg=row["votos_mg"],
                porcentaje_sdd=row["porcentaje_sdd"],
                votos_sdd=row["votos_sdd"],
                porcentaje_avnzr=row["porcentaje_avnzr"],
                votos_avnzr=row["votos_avnzr"],
                porcentaje_nau=row["porcentaje_nau"],
                votos_nau=row["votos_nau"],
                porcentaje_surgencia=row["porcentaje_surgencia"],
                votos_surgencia=row["votos_surgencia"],
                porcentaje_nulo=row["porcentaje_nulo"],
                votos_nulo=row["votos_nulo"],
                porcentaje_blanco=row["porcentaje_blanco"],
                votos_blanco=row["votos_blanco"],
            )
            eleccion.save()
