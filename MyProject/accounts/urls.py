from django.urls import path, include

from MyProject.accounts.views import SingInView, SignUpView, LogoutView, UserDeleteView, UserEditView, UserDetailsView

urlpatterns = (
    path('login/', SingInView.as_view(), name='login page'),
    path('register/', SignUpView.as_view(), name='register page'),
    path('logout/', LogoutView.as_view(), name='logout view'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details view'),
        path('delete/', UserDeleteView.as_view(), name='delete view'),
        path('edit/', UserEditView.as_view(), name='edit view'),
    ])),
)

