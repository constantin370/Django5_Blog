from django.shortcuts import redirect

from django.views.generic import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.utils import CheckUsersMixin

class DeleteManagerPostView(CheckUsersMixin, LoginRequiredMixin, DeleteView):
    """Класс удаления статей."""
    template_name = "users/deletepost.html"
    model = Post
    success_url = "/manager/"
