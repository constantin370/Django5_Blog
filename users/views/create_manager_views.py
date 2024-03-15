from django.shortcuts import redirect

from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm

from users.utils import CheckUsersMixin


class CreateManagerPostView(CheckUsersMixin, LoginRequiredMixin, CreateView):
    """Класс добавления стетей."""
    template_name = "users/addpost.html"
    model = Post
    forms = PostForm
    success_url = "/manager/"
    fields = ["title", "text", "image", "publish"]

    def form_valid(self, form):
        """Если форма допустима, сохраните связанную модель."""
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CreateManagerPostView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Метод проверки пользователей на доступ
        к возможности добавить статью."""
        if self.request.user.is_superuser or self.request.user.is_superuser or self.request.user.is_prof_union:
            return super().post(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")