from django.urls import path

from MyProject.actors.views import ActorsListView, actor_details

urlpatterns = (path('', ActorsListView.as_view(), name='list of actors'),
               path('details/<int:actor_id>/', actor_details, name='actor details'),
               )
