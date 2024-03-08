from django import forms

from blog.models import Post

from users.models import CustomUser


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования статей."""
    class Meta:
        model = Post
        fields = ["title", "text", "publish"]
        # Убрать поля exclude = [""]


class UserRegisterForm(forms.ModelForm):
    """Класс который представляет собой форму регистрации пользователей."""
    password_1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Повторите Пароль", widget=forms.PasswordInput)

    def clean_password_2(self) -> str:
        """Метод clean_password_2, который проверяет,
        совпадают ли введенные пароли. Если они не совпадают,
        то мы вызываем ошибку ValidationError."""

        cd = self.cleaned_data
        if cd['password_1'] != cd["password_2"]:
            raise forms.ValidationError("Ваши пароли не совпадают!")
        return cd["password_2"]
    
    def save(self, commit=True):
        """Метод save используется для сохранения данных пользователя.
        Мы устанавливаем для пользователя пароль, который он ввел
        в поле password_1. Если параметр commit равен True, то мы
        сохраняем пользователя в базе данных."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password_1"])
        if commit:
            user.save()
        return user
    
    class Meta:
        """В классе Meta мы указываем модель CustomUser
        и поля, которые должны отображаться на форме -
        email и username."""
        model = CustomUser
        fields = ('email', 'username',)