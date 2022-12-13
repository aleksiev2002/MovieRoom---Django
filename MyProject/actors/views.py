from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

from MyProject.actors.models import Actor


class ActorsListView(LoginRequiredMixin, views.ListView):
    redirect_field_name = 'nextpage'
    queryset = Actor.objects.order_by('?')[:20]
    template_name = 'actors/list-actors.html'



def actor_details(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    context = {
        'actor': actor,
    }
    return render(request, 'actors/actor-details.html', context)



