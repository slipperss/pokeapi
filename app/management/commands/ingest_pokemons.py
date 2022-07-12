from django.core.management.base import BaseCommand
from django.conf import settings

import json

from app.models import Pokemon


# заносим покемоны в базу данных из json
class Command(BaseCommand):
    help = 'Create tracks from JSON file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'pokemons.json'
        assert datafile.exists()
        with open(datafile, 'r') as f:
            data = json.load(f)

        pokemons = (Pokemon(**pokemon) for pokemon in data)

        Pokemon.objects.bulk_create(pokemons)
