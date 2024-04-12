import pywhatkit
import string
import secrets

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_email_for_verify(request, user):
    """Создание токена для подтверждения почты."""
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user)
    }

    message = render_to_string('users/verify_email.html', context=context)
    email = EmailMessage('Verify email', message, to=[user.email])
    email.send()


def generate_user_login_password(request, user):
    """Фукнция генерации логина и пароля
    для пользоватлей зарегестрировавшихся по номеру телефона."""

    if user.phone_number is not None:

        password = string.ascii_letters + string.digits
        new_pass = ''.join(secrets.choice(password) for i in range(8))

        user.set_password(new_pass)
        user.save(update_fields=["username", "password"])

        return pywhatkit.sendwhatmsg_instantly(phone_no=f'{user.phone_number}',
                                        message=f'пароль: {new_pass}',
                                        wait_time=50)