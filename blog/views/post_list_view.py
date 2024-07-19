from django.http import HttpResponse
from django.views.generic import ListView

from blog.models.post_model import Post

# Create your views here.

class PostListView(ListView):
    """Публикации пользователей на главной странице."""
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(publish=True).order_by("-id").select_related()
    paginate_by = 3
    
