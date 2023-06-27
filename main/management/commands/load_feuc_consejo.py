from csv import DictReader
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
import pandas as pd
import os
from json import loads, dumps

# Import the model
from main.models import Consejo_FEUC, Votaciones_FEUC


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from xlsx of FEUC consejo into our database"

    def add_arguments(self, parser):
        parser.add_argument(
            "path", type=str, help="Indicates the path of the file to be imported"
        )
        parser.add_argument(
            "ano", type=int, help="Indicates the year of the data to be imported"
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
        Consejo_FEUC.objects.filter(ano=options["ano"]).delete()
        consejo_feuc = Consejo_FEUC.objects.create(ano=options["ano"])
        consejo_feuc.save()
        for votacion_index, abstengo in zip(votaciones, abstengos):
            votacion = df.loc[:, votacion_index:abstengo]
            votaciones_finales = pd.concat([votaciones_finales, votacion], axis=1)
            votacion.columns = votacion.iloc[0]
            votacion = votacion.drop(votacion.index[0:101])
            votacion = votacion.drop(votacion.index[[1, 2]])
            resultado_votacion = votacion.to_json(orient="columns")
            modelo_votacion = Votaciones_FEUC.objects.create(
                consejo=consejo_feuc,
                votacion=votacion_index,
                votos=resultado_votacion,
            )
            modelo_votacion.save()
        os.makedirs("../datos/processed", exist_ok=True)
        votaciones_finales.to_csv("../datos/processed/votaciones_consejo.csv")
        print("Processed data backup successfully")
        print("Data imported successfully")
