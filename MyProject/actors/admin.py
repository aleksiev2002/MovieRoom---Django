from django.contrib import admin

from MyProject.actors.models import Actor


@admin.register(Actor)
class AdminActors(admin.ModelAdmin):
    pass
