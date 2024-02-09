
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post

# Create your views here.


class HomeManagerView(LoginRequiredMixin, ListView):
    """Класс представления если пользователь залогинен."""
    model = Post
    template_name = "users/index.html"
    context_object_name = "posts"






