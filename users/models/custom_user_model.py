from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models.user_manager_model import UserManager


class CustomUser(AbstractUser):
    """Настраиваемая модель пользователя."""

    objects = UserManager

    email = models.EmailField(verbose_name="Эллектронная почта", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="пользователи"




