from django.urls import path

from users.views.home_manager_view import HomeManagerView

from users.views.create_manager_views import CreateManagerPostView 

from users.views.update_manager_view import UpdateManagerPostView

from users.views.delete_post_view import DeleteManagerPostView

from users.views.register_user_view import register_user_view

from users.views.register_confirm_view import register_confirm


# from users.views.register_create_user_view import RegistrationView


app_name = "users"


urlpatterns = [
    path('', HomeManagerView.as_view(), name='homemanager'),
    path('addpost/', CreateManagerPostView.as_view(), name='addpost'),
    path('updatepost/<int:pk>/', UpdateManagerPostView.as_view(), name='updatepost'),
    path('deletepost/<int:pk>/', DeleteManagerPostView.as_view(), name='deletepost'),
    # path('register/', RegistrationView.as_view(), name='register'),
    path('register/', register_user_view, name='register'),
    path('register_confirm/', register_confirm, name='register_confirm'),

]

