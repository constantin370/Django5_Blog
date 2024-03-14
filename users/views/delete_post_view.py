from django.shortcuts import redirect

from django.views.generic import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post


class DeleteManagerPostView(LoginRequiredMixin, DeleteView):
    """Класс удаления статей."""
    template_name = "users/deletepost.html"
    model = Post
    success_url = "/manager/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_superuser or self.request.user.is_prof_union:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("blog:main_page")