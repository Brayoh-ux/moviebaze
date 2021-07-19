from django.urls import path
from .views import (
    index, search,
    genres
)

urlpatterns = [
    path('', index, name='home'),
    path('search', search, name='search'),
    path('genres', genres, name='genres')
]