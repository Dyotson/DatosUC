# DatosUC

Pagina web para almacenar toda la información relacionada a datos producidos por los alumnos en las diferentes instancias universitarias (Votaciones, numero de alumnos, PPA, etc.)

# Como montar en local

1. Crear un venv para el proyecto
2. Crear un .env dentro de la carpeta 'DatosUC' con la siguiente información:

```
DJANGO_SECRET_KEY=<Tu Django Secret Key>
DEBUG=True
DJANGO_DB_NAME=datosuc
DJANGO_DB_USER=<El username de tu PostgreSQL>
DJANGO_DB_PASSWORD=<El password de tu PostgreSQL>
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=5432
```

3. Instalar los paquetes necesarios con pip

```
pip install -r requirements.txt
```
