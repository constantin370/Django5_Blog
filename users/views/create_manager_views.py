from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm


class CreateManagerPostView(LoginRequiredMixin, CreateView):
    """Класс добавления стетей."""
    model = Post
    template_name = "users/addpost.html"
    forms = PostForm
    success_url = "/manager/"
    fields = ["title", "text", "publish"]

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CreateManagerPostView, self).form_valid(form)
    

