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
