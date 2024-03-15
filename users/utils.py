from django.shortcuts import redirect

from django.views import View


class CheckUsersMixin(View):
    """Класс Mixin проверки пользоватлей на доступ."""

    def get(self, request, *args, **kwargs):
        """Метод проверки пользоватлей на доступ
        к просмотру добавления записей."""
        if self.request.user.is_superuser or self.request.user.is_superuser or self.request.user.is_prof_union:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")
