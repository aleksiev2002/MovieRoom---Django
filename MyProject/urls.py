from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyProject.common.urls')),
    path('accounts/',  include('MyProject.accounts.urls')),
    path('movies/', include('MyProject.movies.urls')),
    path('actors/', include('MyProject.actors.urls')),
    path('data/', include('MyProject.data.urls')),
]

