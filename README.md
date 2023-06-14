# run in local

## Install Poetry

    curl -sSL https://install.python-poetry.org | python3 -
    or
    pip install poetry

## Install library

    poetry config virtualenvs.in-project true
    poetry install

## pgadmin

    pip3 install psycopg2-binary

## Active library

    poetry shell

## Check data status

    python ./app/backend_pre_start.py

## Run migrations

    alembic upgrade head

## Initial data

    python ./app/initial_data.py

## Start

    uvicorn app.main:app --reload

If you created a new model in `./backend/app/app/models/`, make sure to import it in `./backend/app/app/db/base.py`, that Python module (`base.py`) that imports all the models will be used by Alembic.

After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

    alembic revision --autogenerate -m "Add customm"

# Run job queue 

    rq worker --url redis://localhost:6379/1


                   Installation on Linux:
                   apt-get install tesseract-ocr libtesseract-dev poppler-utils

                   Installation on MacOS:
                   brew install tesseract