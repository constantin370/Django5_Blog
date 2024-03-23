from django.views.generic import CreateView

from users.mixins import LoginRequiredMixin

from blog.models import Post

from users.forms import PostForm


class CreateManagerPostView(LoginRequiredMixin, CreateView):
    """Класс добавления стетей."""
    template_name = "users/addpost.html"
    model = Post
    forms = PostForm
    success_url = "/manager/"
    fields = ["title", "text", "image", "publish"]

    def form_valid(self, form):
        """Если форма допустима, сохраните связанную модель."""
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CreateManagerPostView, self).form_valid(form)