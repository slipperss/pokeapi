from django.contrib import admin

from app.models import UserProfile, Pokemon, PokemonAbility

admin.site.register(UserProfile)
admin.site.register(Pokemon)
admin.site.register(PokemonAbility)
