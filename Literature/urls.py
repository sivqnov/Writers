from django.urls import path
from .views import *

urlpatterns = [
    path('writers', writers, name='writers'),
    path('author/<int:author_id>', view_author, name='author'),
    path('genres', genres, name='genres'),
    path('genre/<int:genre_id>', view_genre, name='genre'),
    path('works', works, name='works'),
    path('work/<int:work_id>', view_work, name='work'),
]