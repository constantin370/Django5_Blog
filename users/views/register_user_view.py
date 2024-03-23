from django.shortcuts import render, redirect

from users.forms import UserRegisterForm

from django.contrib import messages

from django.core.mail import send_mail

from django.urls import reverse

import uuid


TOKEN = uuid.uuid4().hex


def register_user_view(request):
    """Функция регистрации пользователя."""
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            content = reverse("users:register_confirm", kwargs={'token': TOKEN})
            message = (f"Folow to confirm link {user_form.cleaned_data['username']} %s \n"
                     f"to confirm http://127.0.0.1:8000{content}")

            send_mail(
                subject='Another Beatles member',
                message=message,
                from_email='birthday_form@acme.not',
                recipient_list=[user_form.cleaned_data['email']],
                fail_silently=True,
            )
            
            user_form = user_form.save()
            messages.success(request, ('На Ваш email отправленно письмо!'))
            return redirect('login')
    else: 
        user_form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': user_form})




