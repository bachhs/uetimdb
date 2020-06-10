from django.urls import path
from .views import MovieList, MovieDetail, MovieSearch, NameList, NameDetail

app_name = 'imdb'

urlpatterns = [
    path('movie/', MovieList.as_view(), name='movie_list'),
    path('movie/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('name/', NameList.as_view(), name='name_list'),
    path('name/<int:pk>', NameDetail.as_view(), name='name_detail'),
]
