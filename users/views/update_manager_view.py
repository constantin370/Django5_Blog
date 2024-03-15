from django.shortcuts import redirect

from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from users.utils import CheckUsersMixin

from blog.models import Post

from users.forms import PostForm


class UpdateManagerPostView(CheckUsersMixin, LoginRequiredMixin, UpdateView):
    """Класс редактирования статей."""
    template_name = "users/addpost.html"
    model = Post
    forms = PostForm
    success_url = "/"
    fields = ["title", "text", "image", "publish"]