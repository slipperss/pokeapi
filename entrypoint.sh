#!/bin/bash
python manage.py makemigrations app
python manage.py migrate
python manage.py ingest_pokemons
python manage.py runserver 0.0.0.0:8000
