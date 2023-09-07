from django.urls import path, include
from . import views
from djoser.views import UserCreateView, UserLoginView, UserLogoutView, UserDeleteView

urlpatterns = [
    path('auth/register/', UserCreateView.as_view(), name='user-create'),
    path('auth/login/', UserLoginView.as_view(), name='user-login'),
    path('auth/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('auth/delete/', UserDeleteView.as_view(), name='user-delete'),
]