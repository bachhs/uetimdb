from django.urls import path
from .views import MovieList, MovieDetail, MovieSearch

app_name = 'imdb'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
]
