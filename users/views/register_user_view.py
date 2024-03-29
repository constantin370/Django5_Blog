from django.shortcuts import render

from users.forms import UserRegisterForm


def register_user_view(request):
    """Функция регистрации пользователя."""
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form = user_form.save()
            return render(request, 'users/rigister_complite.html')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': user_form})




