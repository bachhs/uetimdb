from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:id_movie>', MovieDetail.as_view(), name='movie_detail'),
]
