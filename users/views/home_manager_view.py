from django.shortcuts import redirect

from django.views.generic import ListView

from blog.models import Post

from users.mixins import LoginRequiredMixin


class HomeManagerView(LoginRequiredMixin, ListView):
    """Класс представления если пользователь залогинен."""
    template_name = "users/index.html"
    model = Post
    context_object_name = "posts"
    
    def get_queryset(self):
        """Возвращает список элементов для этого представления.
        Возвращаемое значение должно быть итеративным
        и может быть экземпляром `QuerySet` в этом случае будет
        включено специфическое поведение `QuerySet'."""
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_prof_union: # noqa
            queryset = Post.objects.filter(user=self.request.user).order_by("-id") # noqa
            return queryset
        else:
            return redirect("blog:main_page")





