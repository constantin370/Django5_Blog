from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from users.forms import UserRegisterForm
from users.utils import send_email_for_verify
from users.models.custom_user_model import CustomUser


class RegistrationView(View):
    """Класс регистрации пользователя."""
    template_name = 'users/register.html'

    def get(self, request):
        context = {
            "form": UserRegisterForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            user = get_object_or_404(CustomUser, email=email)
            send_email_for_verify(request, user)
            messages.info(request, "Вам на email отправленно письмо с сылкой для авторизации!")
            return redirect('blog:main_page')
        
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
    
