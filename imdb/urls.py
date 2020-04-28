from django.urls import path
from .views import MovieList, MovieDetail

app_name = 'imdb'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
]
