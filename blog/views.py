from django.views.generic import ListView
from blog.models.post_model import Post

# Create your views here.

class PostView(ListView):
    """Публикация."""
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"