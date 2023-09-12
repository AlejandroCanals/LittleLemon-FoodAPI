from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/category/', views.CategoryView.as_view()),
    path('menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),

    path('groups/managers/users/', views.ManagerUserListView.as_view(), name='manage-group-list'),
    
    path('groups/managers/users/<int:pk>/', views.ManagerDeleteView.as_view(), name='delete-manager')

        # User group management endpoints

]
