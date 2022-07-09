from django.contrib import admin
from .yasg import urlpatterns as doc_urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/", include("app.urls"))
]
urlpatterns += doc_urls
