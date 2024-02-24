from django.views.generic import ListView

from blog.models.post_model import Post


class PostListViewForCustumUser(ListView):
    """Представление записей определенного пользователя."""
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        return Post.objects.filter(publish=True, user__pk=pk).order_by("-id")