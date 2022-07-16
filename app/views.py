from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerProfileOrReadOnly
from .services import get_or_create_pokemon_for_user


class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def put(self, request, *args, **kwargs):
        obj = get_or_create_pokemon_for_user(request)
        if obj is not None:
            request.POST._mutable = True
            request.data['pokemon'] = obj.id
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        obj = get_or_create_pokemon_for_user(request)
        if obj is not None:
            request.POST._mutable = True
            request.data['pokemon'] = obj.id
        return self.partial_update(request, *args, **kwargs)
