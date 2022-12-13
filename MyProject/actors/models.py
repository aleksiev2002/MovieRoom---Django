from django.db import models

from MyProject.settings import TMDB_IMAGE_PATH


class Actor(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    biography = models.TextField(
        blank=False,
        null=False
    )
    birthday = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    deathday = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    place_of_birth = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    profile_path = models.URLField(blank=False, null=False)
    tmdb_id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

    def movie_image(self):
        return f"{TMDB_IMAGE_PATH}{self.profile_path}"