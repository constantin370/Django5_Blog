from django.urls import path, include
from . import views
from users.views.home_manager_view import HomeManagerView
from users.views.logout_manager_view import logout_view


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', HomeManagerView.as_view(), name='homemanager'),
    path('accounts/logout/', views.logout_view, name='logout'),
]

