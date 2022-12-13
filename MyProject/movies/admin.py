from django.contrib import admin

from MyProject.movies.models import Movie, Genre


@admin.register(Movie)
class AdminMovies(admin.ModelAdmin):
    pass


@admin.register(Genre)
class AdminGenres(admin.ModelAdmin):
    pass
