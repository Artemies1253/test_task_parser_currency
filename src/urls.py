from django.urls import path, include


urlpatterns = [
    path("currency/", include("src.parsers.urls")),
]
