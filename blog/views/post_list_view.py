from django.views.generic import ListView
from blog.models.post_model import Post

# Create your views here.

class PostListView(ListView):
    """Публикации."""
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"