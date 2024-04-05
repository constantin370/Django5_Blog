from django.views.generic import UpdateView
from users.mixins import CustomLoginReqMixin
from users.forms import UpdateUserForm
from users.models.custom_user_model import CustomUser


class UpdateUserView(CustomLoginReqMixin, UpdateView):
    """Класс редактирования статей."""
    template_name = "users/update_user.html"
    model = CustomUser
    form_class = UpdateUserForm
    success_url = "/"