from django.views.generic import DeleteView

from blog.models import Post

from users.mixins import LoginRequiredMixin


class DeleteManagerPostView(LoginRequiredMixin, DeleteView):
    """Класс удаления статей."""
    template_name = "users/deletepost.html"
    model = Post
    success_url = "/manager/"
