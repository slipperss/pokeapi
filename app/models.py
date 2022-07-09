from django.db import models
from django.contrib.auth.models import User


class Pokemon(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(max_length=350, blank=True, null=True, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.PROTECT, related_name="pokemon_id", blank=True, null=True, default=None
    )

    def __str__(self):
        return f"{self.user.username} ({self.user.email})"