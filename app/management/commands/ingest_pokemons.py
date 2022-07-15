import requests
import json

from django.core.management.base import BaseCommand
from django.conf import settings

from app.models import Pokemon, PokemonAbility


# заносим покемоны в базу данных из json
class Command(BaseCommand):
    help = 'Create tracks from JSON file'

    def handle(self, *args, **kwargs):
        pokemons_datafile = settings.BASE_DIR / 'data' / 'pokemons.json'
        assert pokemons_datafile.exists()
        with open(pokemons_datafile, 'r') as f:
            pokemons = json.load(f)
        for i in pokemons:
            i.pop('url')

        pokemon_abilities_datafile = settings.BASE_DIR / 'data' / 'pokemon_abilities.json'
        assert pokemon_abilities_datafile.exists()
        with open(pokemon_abilities_datafile, 'r') as f:
            abilities = json.load(f)

        pokemons = (Pokemon(**pokemon_name) for pokemon_name in pokemons)
        abilities = (PokemonAbility(**ability) for ability in abilities)
        Pokemon.objects.bulk_create(pokemons)
        PokemonAbility.objects.bulk_create(abilities)


        # парсинг данных abilitie покемонов с https://pokeapi.co/api/v2/pokemon/1/
        # main_data = []
        # for url in range(1, 201):
        #     response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{url}/')
        #     example = response.json()['abilities']
        #     for i in example:
        #         main_data.append({'pokemon_id': url, 'name': i['ability']['name']})
        #         print(i['ability']['name'])
        # print(main_data)
        # data_abilities_file = settings.BASE_DIR / 'data' / 'pokemon_abilities.json'
        # assert data_abilities_file.exists()
        # with open(data_abilities_file, 'w') as f2:
        #     print(json.dump(main_data, f2, indent=4))
