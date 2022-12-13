from django.urls import path

from MyProject.movies.views import movie_details, MovieCreateView, MovieListView

urlpatterns = (
    path("details/<int:movie_id>/", movie_details, name='movie_details'),
    path("create/", MovieCreateView.as_view(), name='create_movie'),
    path("", MovieListView.as_view(), name='movie_list'),

)