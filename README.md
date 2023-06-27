# DatosUC

Pagina web para almacenar toda la información relacionada a datos producidos por los alumnos en las diferentes instancias universitarias (Votaciones, numero de alumnos, PPA, etc.)

## Como montar en local

    1. Instala ==Poetry== en tu sistema.
        ```
        curl -sSL https://install.python-poetry.org | python3 -
        ```
    2. Ve al directorio donde esta el proyecto de Github
        ```
        cd DatosUC/
        ```
    3. Inicia ==Poetry==
        ```
        poetry init
        ```
    4. Corre el servidor
        ```
        poetry run ./manage.py runserver
        ```

## Funciones importantes

    - Importar datos consejos FEUC:
        ```
        poetry run ./manage.py load_feuc_consejo datos/<Nombre Archivo> <Año>
        ```
    - Importar datos elecciones FEUC:
        ```
        poetry run ./manage.py load_feuc_results datos/elecciones_feuc.csv
        ```
