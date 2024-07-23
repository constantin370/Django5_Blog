from django.views.generic import UpdateView
from users.mixins import CustomLoginReqMixin
from users.forms import UpdateUserForm
from users.models.custom_user_model import CustomUser
from django.shortcuts import get_object_or_404


class UpdateUserView(CustomLoginReqMixin, UpdateView):
    """Класс редактирования статей."""
    template_name = "users/update_user.html"
    model = CustomUser
    form_class = UpdateUserForm
    success_url = "/"

    def get_object(self, queryset=None):
        if not hasattr(self, '_object'):
            self._object = CustomUser.objects.select_related("discont_card").get(
                id=self.request.user.id
                )
            return self._object
