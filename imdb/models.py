from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Movie(models.Model):
    id_movie = models.IntegerField(primary_key=True, unique=True)
    judul_movie = models.CharField(max_length=200, null=False)
    tahun_movie = models.CharField(max_length=20, null=True)
    gross_movie = models.IntegerField(null=True)
    rating_movie = models.FloatField(null=True)
    meta_movie = models.FloatField(null=True)
    vote_movie = models.IntegerField(null=True)
    rate_movie = models.CharField(max_length=50, null=True)
    durasi_movie = models.CharField(max_length=50, null=True)
    deskripsi_movie = models.TextField(null=True)
    link_movie = models.CharField(max_length=200, null=True)
    poster_movie = models.TextField(null=True)
    dt_movie = models.DateTimeField(null=True)

    def __str__(self):
        return self.judul_movie


class Genre(models.Model):
    id_genre = models.IntegerField(primary_key=True)
    nama_genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nama_genre


class Name(models.Model):
    id_name = models.IntegerField(primary_key=True)
    nama_name = models.CharField(max_length=100, null=True)
    dob_name = models.DateField(null=True)
    pob_name = models.CharField(max_length=500, null=True)
    dod_name = models.DateField(null=True)
    pod_name = models.CharField(max_length=500, null=True)
    birth_name_name = models.CharField(max_length=200, null=True)
    height_name = models.CharField(max_length=20, null=True)
    bio_name = models.TextField(null=True)
    poster_name = models.TextField(null=True)
    link_name = models.TextField(null=True)

    def __str__(self):
        return self.nama_name


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
