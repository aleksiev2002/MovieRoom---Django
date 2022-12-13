from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from MyProject.accounts.forms import MovieRoomUserCreateForm
UserModel = get_user_model()


class SingInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = MovieRoomUserCreateForm
    success_url = reverse_lazy('index')


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/delete-user-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserEditView(views.UpdateView):
    template_name = 'accounts/edit-user-page.html'
    model = UserModel
    fields = ('first_name', 'last_name',)

    def get_success_url(self):
        return reverse_lazy('user details view', kwargs={
            'pk': self.request.user.pk,
        })


class UserDetailsView(views.DetailView):
    template_name = 'accounts/details-user-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


