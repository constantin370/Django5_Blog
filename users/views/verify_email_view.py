from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.utils.http import urlsafe_base64_decode

from users.models.custom_user_model import CustomUser
from users.utils import generate_discont_number


class VerifyEmailView(View):
    """Класс получания пользователя по uid."""
    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
            user = None
        return user

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.discont_card = generate_discont_number()
            user.save()
            login(request, user)
            messages.success(request, "Ваш Аккаунт активен!")
            return redirect('blog:main_page')
        messages.error(request, "Ваша ссылка не корректна, залогиньтесь снова")
        return redirect('blog:main_page')