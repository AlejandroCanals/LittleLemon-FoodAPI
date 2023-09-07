from rest_framework import serializers
from .models import MenuItem, Category, Cart
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

#Creacion de Serializers
"""Convierten los objetos complejos como los modelos de las base de datos de 
#django en formados de datos mas simples como JSON ."""

class UserSerializer(UserCreateSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'featured', 'category']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
