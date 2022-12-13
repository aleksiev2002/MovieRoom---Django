from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass
