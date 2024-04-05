from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from blog.models import Post
from users.models.custom_user_model import CustomUser


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования статей."""
    class Meta:
        model = Post
        fields = ["title", "text", "image", "publish"]
        # Убрать поля exclude = [""]


class UserRegisterForm(forms.ModelForm):
    """Класс который представляет собой форму регистрации пользователей."""
    email = forms.EmailField(label=_("Email"),
                             help_text="Все поля со звездочкой обязательны к заполнению!",
                              max_length=254,
                              widget=forms.EmailInput(attrs={'autocomplete': 'email'},)
                              )

    password1 = forms.CharField(label="Пароль: ",
                                 widget=forms.PasswordInput,
                                 help_text=password_validation.password_validators_help_text_html())
    
    password2 = forms.CharField(label="Повторите пароль:",
                                 widget=forms. PasswordInput,
                                 help_text="Для проверки введите пороль еще раз")

    def clean_password(self):
        """Метод проверки пароля."""
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
            return password1
        
    def clean(self):
        """Метод сверки паролей."""
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            error = {'password2': ValidationError("Введеные пароли не совподают",
                                                  code="password_mismatch")}
            raise ValidationError(error)
        
    def save(self, commit=True):
        """Метод save используется для сохранения данных пользователя.
        Мы устанавливаем для пользователя пароль, который он ввел
        в поле password_1. Если параметр commit равен True, то мы
        сохраняем пользователя в базе данных."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    class Meta:
        """В классе Meta мы указываем модель CustomUser
        и поля, которые должны отображаться на форме -
        email и username."""
        model = CustomUser
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
            )
        

class UpdateUserForm(forms.ModelForm):
    """Форма редактирования данных пользователя."""
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']