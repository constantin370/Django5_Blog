from django.shortcuts import redirect

from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm


class UpdateManagerPostView(LoginRequiredMixin, UpdateView):
    """Класс редактирования статей."""
    template_name = "users/addpost.html"
    model = Post
    forms = PostForm
    success_url = "/"
    fields = ["title", "text", "image", "publish"]

    def get(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_superuser or self.request.user.is_prof_union:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")