from users.views.home_manager_view import HomeManagerView
from users.views.create_manager_views import CreateManagerPostView
from users.views.update_manager_view import UpdateManagerPostView
from users.views.register_create_user_view import RegistrationView
from users.views.verify_email_view import VerifyEmailView
from users.views.update_user_view import UpdateUserView


__all__ = (
    "HomeManagerView",
    "CreateManagerPostView",
    "UpdateManagerPostView",
    "RegistrationView",
    "VerifyEmailView",
    "UpdateUserView",
)