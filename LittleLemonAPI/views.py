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

#Cart
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = CartAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



#Managers

class ManagerUserListView(generics.ListCreateAPIView):
    serializer_class = GroupsSerializer
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
                return Response({"error": "Username does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Agregar el usuario al grupo de Managers
            managers_group = Group.objects.get(name='Managers')
            user.groups.add(managers_group)

            return Response({"message": f"User {username} added to the Managers group."}, status=status.HTTP_201_CREATED)
    

class ManagerDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]  # Ajusta los permisos según tus necesidades
    serializer_class = GroupsSerializer

    def get_queryset(self):
        # Obtén el grupo de Managers
        managers_group = Group.objects.get(name='Managers')
        return User.objects.filter(groups=managers_group)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "Username does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Eliminar el usuario del grupo de Managers
        managers_group = Group.objects.get(name='Managers')
        instance.groups.remove(managers_group)

        return Response({"message": f"User {instance.username} was deleted from Managers."}, status=status.HTTP_200_OK)


#Delivery Group

class DeliveryUserListView(generics.ListCreateAPIView):

    serializer_class = GroupsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # Obtén el grupo de Managers
        Delivery_crew_group = Group.objects.get(name='Delivery Crew')
        return User.objects.filter(groups=Delivery_crew_group)

    def create(self, request, *args, **kwargs):
            # Obtener el username del usuario que se va a agregar al grupo de Managers
            username = request.data.get('username')

            # Verificar si el usuario ya existe
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"error": "Username does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Agregar el usuario al grupo de Managers
            Delivery_crew_group = Group.objects.get(name='Delivery Crew')
            user.groups.add(Delivery_crew_group)

            return Response({"message": f"User {username} added to the Delivery group."}, status=status.HTTP_201_CREATED)  

class DeliveryDeleteView(generics.DestroyAPIView):
    
    permission_classes = [IsAdminUser]  
    serializer_class = GroupsSerializer

    def get_queryset(self):
        # Obtén el grupo de Managers
        Delivery_crew_group = Group.objects.get(name='Delivery Crew')
        return User.objects.filter(groups=Delivery_crew_group)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "Username does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Eliminar el usuario del grupo de Managers
        Delivery_crew_group = Group.objects.get(name='Delivery Crew')
        instance.groups.remove(Delivery_crew_group)

        return Response({"message": f"User {instance.username} was deleted from Delivery-Crew."}, status=status.HTTP_200_OK)

