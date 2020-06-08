from django.urls import path
from .views import MovieList, MovieDetail, MovieSearch, NameDetail

app_name = 'imdb'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('name/<int:pk>', NameDetail.as_view(), name='name_detail'),
]
