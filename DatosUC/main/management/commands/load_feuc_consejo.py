from csv import DictReader
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
import pandas as pd
import os

# Import the model
from main.models import Consejo_FEUC


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from xlsx of FEUC consejo into our database"

    def add_arguments(self, parser):
        parser.add_argument(
            "path", type=str, help="Indicates the path of the file to be imported"
        )

    def handle(self, *args, **options):
        # Code to load the data into database
        print("Importing data from", options["path"])
        df = pd.read_excel(options["path"], sheet_name="Consolidado al 10-06")
        votaciones = df.filter(regex="\)")
        votaciones = votaciones.columns
        votaciones = list(votaciones)
        abstengos = df.columns[df.isin(["Abstengo"]).any()]
        abstengos = list(abstengos)
        votaciones_finales = pd.DataFrame()
        for votacion, abstengo in zip(votaciones, abstengos):
            votacion = df.loc[:, votacion:abstengo]
            votaciones_finales = pd.concat([votaciones_finales, votacion], axis=1)
        os.makedirs("../datos/processed", exist_ok=True)
        votaciones_finales.to_csv("../datos/processed/votaciones_consejo.csv")
