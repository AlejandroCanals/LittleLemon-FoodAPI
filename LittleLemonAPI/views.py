from django.shortcuts import render
# Importa ListCreateAPIVIEW, Retrieve ...etc
from rest_framework import generics

# Mis modulos
from .models import MenuItem, Category, Cart
from .serializers import *
from .paginations import MenuItemListPagination
from .permissions import *

# Modulos DRF para los permisos, Throttling
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response

from django.contrib.auth.models import Group, User
# Create your views here


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class MenuItemsView(PermissionMixin, generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category']
    search_fields = ['title', 'category']
    pagination_class = MenuItemListPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

# For individual items
class MenuItemDetailView(PermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


#Managers

class ManagerUserListView(generics.ListCreateAPIView):
    serializer_class = ManagerSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # Obtén el grupo de Managers
        managers_group = Group.objects.get(name='Managers')
        return User.objects.filter(groups=managers_group)

    def create(self, request, *args, **kwargs):
            # Obtener el username del usuario que se va a agregar al grupo de Managers
            username = request.data.get('username')

            # Verificar si el usuario ya existe
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"error": "El usuario no existe."}, status=status.HTTP_400_BAD_REQUEST)

            # Agregar el usuario al grupo de Managers
            managers_group = Group.objects.get(name='Managers')
            user.groups.add(managers_group)

            return Response({"message": f"Usuario {username} agregado al grupo de Managers."}, status=status.HTTP_201_CREATED)
    

class ManagerDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]  # Ajusta los permisos según tus necesidades

    def get_queryset(self):
        # Obtén el grupo de Managers
        managers_group = Group.objects.get(name='Managers')
        return User.objects.filter(groups=managers_group)

    def perform_destroy(self, instance):
        # Eliminar el usuario del grupo de Managers
        managers_group = Group.objects.get(name='Managers')
        instance.groups.remove(managers_group)
