from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm


class UpdateManagerPostView(LoginRequiredMixin, UpdateView):
    """Класс редактирования статей."""
    model = Post
    template_name = "users/addpost.html"
    forms = PostForm
    success_url = "/"
    fields = ["title", "text", "publish"]