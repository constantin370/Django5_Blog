from users.forms import UserRegisterPhoneForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from users.models.custom_user_model import CustomUser
from users.utils import generate_user_login_password
from django.contrib.auth import login
from django.urls import reverse_lazy


def users_register_phone_view(request):
    """Функция регистрации пользователя."""
    if request.method == 'POST':
        form = UserRegisterPhoneForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_superuser = False
            user.is_stuff = False
            user.is_active = True
            form.save()
            phone_number = form.cleaned_data.get("phone_number")
            user = get_object_or_404(CustomUser, phone_number=phone_number)
            messages.info(request, "Вам отправленно SMS с логином и паролем для авторизации!")
            generate_user_login_password(request, user)
            login(request, user)
            return redirect('blog:main_page')
    else:
        form = UserRegisterPhoneForm()
    return render(request, 'users/phone_register.html', {'form': form})