from users.views.home_manager_view import HomeManagerView
from users.views.create_manager_views import CreateManagerPostView
from users.views.update_manager_view import UpdateManagerPostView
from users.views.register_user_view import register_user_view
from users.views.register_create_user_view import RegistrationView
from users.views.register_confirm_view import register_confirm


__all__ = (
    "HomeManagerView",
    "CreateManagerPostView",
    "UpdateManagerPostView",
    "register_user_view",
    "RegistrationView",
    "register_confirm"
)