import tmdbsimple as tmdb
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

from MyProject.movies.forms import MovieCreationForm
from MyProject.movies.models import Movie, Genre
from MyProject.settings import TMDB_IMAGE_PATH

# This is to get the actors and their images from the API
def get_API_actors(movie_id):
    actors = tmdb.Movies(movie_id).credits()
    cast = actors['cast']
    if cast:
        name_list = []
        for x in range(4):
            name_list.append({'name': cast[x]['name'], 'picture': f"{TMDB_IMAGE_PATH}{cast[x]['profile_path']}"})
        return name_list

    return None


def get_API_images(movie_id):
    images = tmdb.Movies(movie_id).images()
    backdrops = images['backdrops']
    image_list = []
    if images['backdrops']:
        for x in range(1):
            image_list.append(f"{TMDB_IMAGE_PATH}{backdrops[x]['file_path']}")
        return image_list
    else:
        return


def get_duration_and_release_date_API(movie_id):
    movie = tmdb.Movies(movie_id).info()
    release_date = movie['release_date']
    duration = movie['runtime']
    return release_date, duration

@login_required
def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie_genres = Genre.objects.filter(movie=movie_id)
    actors = get_API_actors(movie.movie_id)
    other_images = get_API_images(movie.movie_id)
    release_date, duration = get_duration_and_release_date_API(movie.movie_id)
    context = {
        'movie': movie,
        'genres': movie_genres,
        'actors': actors,
        'other_images': other_images,
        'release_date': release_date,
        'duration': duration,
    }
    return render(request, 'movies/movie-details.html', context)


class MovieCreateView(views.CreateView):
    model = Movie
    form_class = MovieCreationForm

    template_name = 'movies/create-movie.html'


class MovieListView(LoginRequiredMixin, views.ListView):
    queryset = Movie.objects.order_by('?')[:20]
    template_name = 'movies/movie-list.html'
