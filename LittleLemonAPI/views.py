from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category,Cart
from .serializers import MenuItemSerializer, CategorySerializer,CartSerializer

# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
