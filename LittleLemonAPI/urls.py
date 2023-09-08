from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('menu-items', views.MenuItemsView.as_view()),
    path('category', views.CategoryView.as_view()),
]
