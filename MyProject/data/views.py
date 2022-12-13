import requests
from django.shortcuts import render
import tmdbsimple as tmdb
from requests import HTTPError

from MyProject.movies import models as movie_models
from MyProject.actors import models as actor_models
from MyProject.settings import TMDB_API_KEY, TMDB_IMAGE_PATH

tmdb.API_KEY = TMDB_API_KEY
image_path = TMDB_IMAGE_PATH
def add_movie(request):

    final_list = []
    n = 0
    while n < 25:
        n += 1
        url = 'http://api.themoviedb.org/3/discover/movie?&sort_by=popularity.desc&offset=20&page={}&api_key='.format(
            n)
        req = requests.get(url + tmdb.API_KEY).json()
        results = req['results']
        final_list.extend(results)
        for movie in results:
            if movie['original_language'] == str('en') and movie['adult'] is False:
                final_list.extend(results)
        print(len(final_list))

    for i in range(500):
        title = final_list[i]['title']
        overview = final_list[i]['overview']
        movie_id = final_list[i]['id']
        is_adult = final_list[i]['adult']
        poster_path = final_list[i]['poster_path']
        genre_ids = final_list[i]['genre_ids']
        movie = movie_models.Movie(title=f'{title}', overview=f"{overview}",
                                   movie_id=f'{movie_id}', is_adult=f'{is_adult}',
                                   poster_path=f'{poster_path}')
        movie.save()
        for g_id in genre_ids:
            movie.genres.add(g_id)
    all_movies = movie_models.Movie.objects.all()

    return render(request, 'movies/import-movies.html', {'movies': all_movies, 'image_path': image_path})


def add_actors(request):
    person_list = []
    person_id = 0
    while True:
        if len(person_list) == 50:
            break

        try:
            person = tmdb.People(person_id).info()
            person_id += 1
            if person['popularity'] > 20:
                person_list.append(person['id'])
        except HTTPError:
            person_id += 1
            continue

    for p_id in person_list:
        p = tmdb.People(p_id).info()
        name = p['name']
        biography = p['biography']
        tmdb_id = p['id']
        birthday = '' if p['birthday'] is None else p['birthday']
        deathday = '' if p['deathday'] is None else p['deathday']
        profile_path = '' if p['profile_path'] is None else p['profile_path']
        place_of_birth = '' if p['place_of_birth'] is None else p['place_of_birth']
        person = actor_models.Actor(name=name, biography=biography,
                                    birthday=birthday, tmdb_id=tmdb_id,
                                    deathday=deathday, profile_path=profile_path,
                                    place_of_birth=place_of_birth
                                    )
        person.save()

    all_actors = actor_models.Actor.objects.all()

    return render(request, 'actors/import-actors.html', {'actors': all_actors})





