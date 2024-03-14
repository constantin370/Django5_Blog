from django.shortcuts import render, redirect

from users.forms import UserRegisterForm

from django.contrib import messages


def register_user_view(request):
    """Функция регистрации пользователя."""
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)  
        if user_form.is_valid():
            user_form = user_form.save()
            messages.success(request, ('На Ваш email отправленно письмо!'))
            return redirect('users:login')
    else: 
        user_form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': user_form})




