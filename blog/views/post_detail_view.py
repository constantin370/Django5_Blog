from django.views.generic import DetailView
from blog.models.post_model import Post


class PostDetailView(DetailView):
    """Публикация."""
    model = Post
    template_name = "blog/single_post.html"
    context_object_name = "post"