from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/", include("app.urls"))
]
urlpatterns += doc_urls
