from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models.user_manager_model import UserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField # type: ignore


class CustomUser(AbstractUser):
    """Настраиваемая модель пользователя."""

    objects = UserManager

    email = models.EmailField(verbose_name="Эллектронная почта", unique=True)

    password = models.CharField(verbose_name="Пароль: ", unique=True, max_length=255)

    phone_number = PhoneNumberField(verbose_name="Номер телефона", unique=True, null=True, blank=False)

    is_prof_union = models.BooleanField(verbose_name="Является профсоюзом", default=False)

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Определяет, следует ли считать этого пользователя активным. '
            'Снимите этот флажок вместо удаления учетных записей.'
        ),
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="пользователи"

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'




