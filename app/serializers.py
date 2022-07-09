from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'description', 'pokemon')