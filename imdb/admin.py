from django.contrib import admin
from .models import Movie, Name, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id_genre', 'nama_genre')
    ordering = ('id_genre', 'nama_genre')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id_movie', 'judul_movie',
                    'tahun_movie', 'rating_movie')
    list_filter = ('rating_movie',)
    search_fields = ('judul_movie', 'id_movie')
    ordering = ('judul_movie', 'rating_movie')


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id_name', 'nama_name', 'dob_name')
    ordering = ('nama_name', 'dob_name')
