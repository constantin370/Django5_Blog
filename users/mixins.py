from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin as CustomLoginReqMixin


class LoginRequiredMixin(CustomLoginReqMixin):
    """Расширинная версия класса LoginRequiredMixin. 
    Убедитесь, что текущий пользователь прошел проверку подлинности,
    а также проверка пользоватлей на доступ к менеджеру статей."""

    def get(self, request, *args, **kwargs):
        """Метод проверки пользоватлей на доступ
        к просмотру добавления записей."""
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_prof_union:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")

    def post(self, request, *args, **kwargs):
        """Метод проверки пользователей на доступ
        к возможности добавить статью."""
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_prof_union:
            return super().post(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")
