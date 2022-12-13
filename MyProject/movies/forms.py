from django import forms

from MyProject.movies.models import Movie


class MovieCreationForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields =['title', 'overview', 'is_adult', 'genres']