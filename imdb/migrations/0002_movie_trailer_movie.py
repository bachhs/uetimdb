# Generated by Django 3.0.5 on 2020-04-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_movie',
            field=models.TextField(null=True),
        ),
    ]
