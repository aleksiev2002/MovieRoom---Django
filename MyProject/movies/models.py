from django.db import models
TMDB_IMAGE_PATH = 'https://image.tmdb.org/t/p/w500'

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    overview = models.TextField()
    is_adult = models.BooleanField()
    movie_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def movie_image(self):
        return f'{TMDB_IMAGE_PATH}{self.poster_path}'


