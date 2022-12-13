import tmdbsimple as tmdb
from django.views import generic as views
from MyProject.actors.models import Actor
from MyProject.movies.models import Movie


def get_upcoming_movies_from_API():
    movies = tmdb.Movies().upcoming()
    upcoming_list = []
    for movie in movies['results']:
        if movie['original_language'] == 'en':
            upcoming_list.append(movie)
        if len(upcoming_list) == 4:
            return upcoming_list


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.order_by('?')[:8]
        context['actors'] = Actor.objects.order_by('?')[:4]
        context['upcoming_movies'] = get_upcoming_movies_from_API()
        return context
