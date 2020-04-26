from django.contrib import admin
from .models import Movie, Name, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id_genre', 'name_genre')
    ordering = ('id_genre', 'name_genre')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id_movie', 'title_movie',
                    'year_movie', 'rating_movie')
    list_filter = ('rating_movie',)
    search_fields = ('title_movie', 'id_movie')
    ordering = ('title_movie', 'rating_movie')


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id_name', 'name_name', 'dateOfBirth_name')
    ordering = ('name_name', 'dateOfBirth_name')
