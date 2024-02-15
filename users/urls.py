from django.urls import path, include

from users.views.home_manager_view import HomeManagerView

from users.views.create_manager_views import CreateManagerPostView 

from users.views.update_manager_view import UpdateManagerPostView

from users.views.delete_post_view import DeleteManagerPostView


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', HomeManagerView.as_view(), name='homemanager'),
    # path('accounts/logout/', views.logout_view, name='logout'),
    path('addpost/', CreateManagerPostView.as_view(), name='addpost'),
    path('updatepost/<int:pk>/', UpdateManagerPostView.as_view(), name='updatepost'),
    path('deletepost/<int:pk>/', DeleteManagerPostView.as_view(), name='deletepost'),

]

