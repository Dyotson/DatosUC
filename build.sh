#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py load_feuc_consejo datos/Consejo_FEUC.xlsx 2023
python manage.py load_feuc_results datos/elecciones_feuc.csv