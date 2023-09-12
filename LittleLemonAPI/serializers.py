from rest_framework import serializers
from .models import MenuItem, Category, Cart
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from . import models
from django.contrib.auth.models import User


#Creacion de Serializers
"""Convierten los objetos complejos como los modelos de las base de datos de 
#django en formados de datos mas simples como JSON ."""

#Usuarios
class UserSerializer(UserCreateSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
    
#Categorias e Items
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']

class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [ 'menuitem', 'quantity','user']