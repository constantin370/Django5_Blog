from django.urls import path
from blog.views.post_list_view import PostListView
from blog.views.post_detail_view import PostDetailView
from blog.views.post_list_view_custom_users import PostListViewForCustumUser

app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name='main_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='single_post'),
    path('cat/<int:pk>/', PostListViewForCustumUser.as_view(), name='cat_post'),
]

