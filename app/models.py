from django.db import models
from django.contrib.auth.models import User


class Pokemon(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(max_length=350, blank=True, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.PROTECT,
                                related_name="pokemon",
                                blank=True,
                                null=True,
                                )

    def __str__(self):
        return f"{self.user.username} ({self.user.email})"
