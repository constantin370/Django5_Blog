from django.views.generic import UpdateView
from blog.models import Post
from users.mixins import LoginRequiredMixin
from users.forms import PostForm


class UpdateManagerPostView(LoginRequiredMixin, UpdateView):
    """Класс редактирования статей."""
    template_name = "users/addpost.html"
    model = Post
    forms = PostForm
    success_url = "/"
    fields = ["title", "text", "image", "publish"]