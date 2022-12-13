from django.urls import path

from MyProject.data.views import add_movie, add_actors

urlpatterns = (
    path('movies/', add_movie, name='import movies'),
    path('actors/', add_actors, name='import actors'),

)
