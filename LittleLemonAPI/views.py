from django.shortcuts import render
#Importa ListCreateAPIVIEW, Retrieve ...etc
from rest_framework import generics

#Mis modulos
from .models import MenuItem, Category,Cart
from .serializers import MenuItemSerializer, CategorySerializer,CartSerializer
from .paginations import MenuItemListPagination
from .permissions import *

#Modulos DRF para los permisos, Throttling 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response 


# Create your views here


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class MenuItemsView(PermissionMixin,generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category'] 
    search_fields = ['title', 'category'] 
    pagination_class = MenuItemListPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

#For individual items
class MenuItemDetailView(PermissionMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer





