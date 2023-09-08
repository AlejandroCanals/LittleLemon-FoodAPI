from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category,Cart
from .serializers import MenuItemSerializer, CategorySerializer,CartSerializer
from .paginations import MenuItemListPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsManager, IsDeliveryCrew
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response 



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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
                permission_classes = [IsAuthenticated, IsAdminUser]
        return[permission() for permission in permission_classes] 
    


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, menuitemId):
        try:
            menu_item = self.queryset.get(pk=menuitemId)
            serializer = self.serializer_class(menu_item)
            return Response(serializer.data)
        except MenuItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, menuitemId):
        try:
            menu_item = self.queryset.get(pk=menuitemId)
            if request.user.is_superuser or request.user.is_staff:
                # Toggle the featured status
                menu_item.featured = not menu_item.featured
                menu_item.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except MenuItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, menuitemId):
        if request.user.is_superuser:
            try:
                menu_item = self.queryset.get(pk=menuitemId)
                menu_item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except MenuItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)



 