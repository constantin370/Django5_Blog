from django.urls import path
from users.views.home_manager_view import HomeManagerView
from users.views.create_manager_views import CreateManagerPostView 
from users.views.update_manager_view import UpdateManagerPostView
from users.views.delete_post_view import DeleteManagerPostView
from users.views.verify_email_view import VerifyEmailView
from django.views.generic import TemplateView
from users.views.register_create_user_view import RegistrationView


app_name = "users"


urlpatterns = [
    path('', HomeManagerView.as_view(), name='homemanager'),
    path('addpost/', CreateManagerPostView.as_view(), name='addpost'),
    path('updatepost/<int:pk>/', UpdateManagerPostView.as_view(), name='updatepost'),
    path('deletepost/<int:pk>/', DeleteManagerPostView.as_view(), name='deletepost'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verifyemail'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirmemail'),
    path('email_confirmed/', TemplateView.as_view(template_name='users/email_confirmed.html'), name='emailconfirmed'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalidverify'),

]

