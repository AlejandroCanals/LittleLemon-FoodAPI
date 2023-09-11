from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category,Cart
from .serializers import MenuItemSerializer, CategorySerializer,CartSerializer
from .paginations import MenuItemListPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response 
from .permissions import *




# Create your views he


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(PermissionMixin,generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category'] 
    search_fields = ['title', 'category'] 
    pagination_class = MenuItemListPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class MenuItemDetailView(PermissionMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer





