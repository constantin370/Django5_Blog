from typing import Any

from django.db.models.query import QuerySet

from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

# Create your views here.


class HomeManagerView(LoginRequiredMixin, ListView):
    """Класс представления если пользователь залогинен."""
    model = Post
    template_name = "users/index.html"
    context_object_name = "posts"
    
    def get_queryset(self, **kwargs) -> QuerySet[Any]:
        queryset = Post.objects.filter(user=self.request.user).order_by("-id")
        return queryset






