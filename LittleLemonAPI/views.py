from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category,Cart
from .serializers import MenuItemSerializer, CategorySerializer,CartSerializer
from .paginations import MenuItemListPagination

# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category'] 
    search_fields = ['title', 'category'] 
    pagination_class = MenuItemListPagination




 