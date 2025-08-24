from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, UserViewSet
from rest_framework.routers import DefaultRouter
from .views import FollowUserView, UnfollowUserView, UserListView



router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
