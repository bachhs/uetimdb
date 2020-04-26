from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Movie(models.Model):
    id_movie = models.IntegerField(primary_key=True, unique=True)
    title_movie = models.CharField(max_length=200, null=False)
    year_movie = models.CharField(max_length=20, null=True)
    gross_movie = models.IntegerField(null=True)
    rating_movie = models.FloatField(null=True)
    meta_movie = models.FloatField(null=True)
    vote_movie = models.IntegerField(null=True)
    rate_movie = models.CharField(max_length=50, null=True)
    duration_movie = models.CharField(max_length=50, null=True)
    description_movie = models.TextField(null=True)
    link_movie = models.CharField(max_length=200, null=True)
    poster_movie = models.TextField(null=True)
    dt_movie = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-year_movie']

    def __str__(self):
        return self.title_movie


class Genre(models.Model):
    id_genre = models.IntegerField(primary_key=True)
    name_genre = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['name_genre']

    def __str__(self):
        return self.name_genre


class Name(models.Model):
    id_name = models.IntegerField(primary_key=True)
    name_name = models.CharField(max_length=100, null=True)
    dateOfBirth_name = models.DateField(null=True)
    placeOfBirth_name = models.CharField(max_length=500, null=True)
    dateOfDeath_name = models.DateField(null=True)
    placeOfDeath_name = models.CharField(max_length=500, null=True)
    birthName_name = models.CharField(max_length=200, null=True)
    height_name = models.CharField(max_length=20, null=True)
    bio_name = models.TextField(null=True)
    poster_name = models.TextField(null=True)
    link_name = models.TextField(null=True)

    class Meta:
        ordering = ['name_name']

    def __str__(self):
        return self.name_name


class Movie_Cast(models.Model):
    id_movie_cast = models.IntegerField(primary_key=True)
    id_name = models.ForeignKey(
        Name, on_delete=models.CASCADE, db_column='id_name')
    id_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, db_column='id_movie')


class Movie_Director(models.Model):
    id_movie_director = models.IntegerField(primary_key=True)
    id_name = models.ForeignKey(
        Name, on_delete=models.CASCADE, db_column='id_name')
    id_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, db_column='id_movie')


class Movie_Genre(models.Model):
    id_movie_genre = models.IntegerField(primary_key=True)
    id_genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, db_column='id_genre')
    id_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, db_column='id_movie')
