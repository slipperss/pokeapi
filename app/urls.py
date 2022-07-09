from django.urls import path

from .views import UserProfileListView, UserProfileDetailView

urlpatterns = [
    path("all-profiles/", UserProfileListView.as_view(), name="all-profiles"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile"),
]
