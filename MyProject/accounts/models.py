from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


class MovieRoomUser(AbstractUser):
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True)
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        validators=(
            validators.MinLengthValidator(3),
        )
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        validators=(
            validators.MinLengthValidator(3),
         )
    )

