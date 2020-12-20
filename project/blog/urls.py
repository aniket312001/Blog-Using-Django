from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name = 'blog/post_detail.html'),name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name = 'blog/post_form.html'),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name = 'blog/post_form.html'),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name = 'blog/post_confirm_delete.html'),name='post-delete'),
    path('about/', views.about_view,name='blog-about'),

]
