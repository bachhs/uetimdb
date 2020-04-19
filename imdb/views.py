from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    paginate_by = 15


class MovieDetail(DetailView):
    model = Movie
    slug_field = 'id_movie'
