from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/category/', views.CategoryView.as_view()),
    path('menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),

        # User group management endpoints
    path('groups/managers/users/', views.ManagerUserListView.as_view(), name='ManagerUserList'),
    path('groups/managers/users/<int:pk>/', views.ManagerDeleteView.as_view(), name='DeleteManager'),
    path('groups/delivery-crew/users/', views.DeliveryUserListView.as_view(), name='DeliveryUserList'),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryDeleteView.as_view(), name='DeliveryDelete'),
    path('cart/menu-items',views.CartView.as_view(), name='CartView')


]
