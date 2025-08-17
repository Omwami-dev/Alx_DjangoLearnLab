from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),                 # List all posts
    path('posts/new/', PostCreateView.as_view(), name='new'),         # Create a new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    # View post details
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='update'),   # Edit post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'), # Delete post
]

