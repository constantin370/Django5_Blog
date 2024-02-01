from django.db import models
from users.models.custom_user_model import CustomUser

class Post(models.Model):
    """Модель Новости."""
    title = models.CharField(verbose_name="Название новости", max_length=150)
    text = models.TextField(verbose_name="Тело статьи")
    # image = models.ImageField(verbose_name="Картинка")
    date_create = models.DateField(verbose_name="Дата создания", auto_now=True)
    data_update = models.DateField(verbose_name="Дата обновления", null=True, blank=True)
    user = models.ForeignKey(CustomUser, verbose_name="Автор", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, название поста: {self.title}"

    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
