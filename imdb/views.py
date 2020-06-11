from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet, Q
from .models import Movie, Name, Genre, Movie_Cast, Movie_Director, Movie_Genre


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


class MovieSearch(ListView):
    model = Movie
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(Q(
                title_movie__icontains=query) | Q(year_movie__icontains=query))
        else:
            object_list = self.model.objects.none()
        return object_list


class NameList(ListView):
    model = Name
    paginate_by = 15


class NameDetail(DetailView):
    model = Name

    def get_object(self):
        object = super(NameDetail, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casted_list'] = Movie_Cast.objects.filter(
            id_name=self.get_object().id_name)
        context['directed_list'] = Movie_Director.objects.filter(
            id_name=self.get_object().id_name)
        return context


class GenreDetail(DetailView):
    model = Genre
    paginate_by = 15

    def get_object(self):
        object = super(GenreDetail, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_list'] = Movie_Genre.objects.filter(
            id_genre=self.get_object().id_genre)
        return context
