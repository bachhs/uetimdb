from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Movie_Cast, Movie_Director, Movie_Genre


class MovieList(ListView):
    model = Movie
    paginate_by = 15


class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cast_list'] = Movie_Cast.objects.filter(
            id_movie=self.get_object().id_movie)
        context['director_list'] = Movie_Director.objects.filter(
            id_movie=self.get_object().id_movie)
        context['genre_list'] = Movie_Genre.objects.filter(
            id_movie=self.get_object().id_movie)
        return context


class MovieGenre(ListView):
    model = Movie

    def get_queryset(self):
        return super().get_queryset()
