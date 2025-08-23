from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
# your existing post views here...
CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("post/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("post/<int:post_id>/comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("post/<int:post_id>/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
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
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # ✅ Create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # ✅ Update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # ✅ Delete
]
