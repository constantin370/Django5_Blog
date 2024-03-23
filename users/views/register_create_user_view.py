from django.urls import reverse_lazy

from django.views.generic.edit import CreateView


from users.forms import UserRegisterForm


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    
