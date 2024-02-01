from django.urls import path
from blog.views.post_list_view import PostListView
from blog.views.post_detail_view import PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='main_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='single_post'),
]