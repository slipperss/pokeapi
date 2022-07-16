import requests

from app.models import Pokemon


def get_or_create_pokemon_for_user(request):
    try:
        offset = int(request.data['pokemon']) - 1  # так как изначально у нас стоит limit 1
        pokemon_amount = 1154  # всего покемонов в апишке
        if offset > pokemon_amount:
            raise IndexError
        print('offset', offset, type(offset))
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=1&offset={offset}')
        pokemon_name = response.json()['results'][0]['name']  # парсим имя покемона с запроса
        obj, _ = Pokemon.objects.get_or_create(name=pokemon_name)  # берем покемона или создаем покемона по имени
        if obj:
            print('success', obj.id, obj.name)
        return obj
    except:
        return None
