from django.views.generic import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm


class DeleteManagerPostView(LoginRequiredMixin, DeleteView):
    """Класс удаления статей."""
    model = Post
    template_name = "users/deletepost.html"
    success_url = "/manager/"