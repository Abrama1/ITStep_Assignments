from django.urls import path
from .views import IndexView, PostDetailView, AddPostView, DeletePostView, MyPostsView, EditPostView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_info"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('myposts/', MyPostsView.as_view(), name='myposts'),
]
