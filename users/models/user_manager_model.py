from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    """Пользовательский менеджер моделей пользователей,
    в котором электронная почта является уникальным
    идентификатором для аутентификации вместо
    имен пользователей."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Создайте и сохраните пользователя с
        указанным адресом электронной почты и паролем."""
        if not email: 
            raise ValueError("Email is not required!")  
        user = self.model(email=self.normalize_email(email), **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    def create_superuser(self, email, password, **extra_fields): 
        """Создайте и сохраните суперпользователя
        с указанным адресом электронной почты и паролем.""" 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_active', True) 
 
        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have is_staff=True.') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
