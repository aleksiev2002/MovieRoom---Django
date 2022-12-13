from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

UserModel = get_user_model()


class MovieRoomUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "username")
        field_classes = {"username": UsernameField}


class MovieRoomUserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': UsernameField}
