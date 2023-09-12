from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Mixin que aplica IsAuthenticated e IsAdminUser como clases de permisos cuando el método de la solicitud no es 'GET',
class PermissionMixin:
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsAdminUser]
        return[permission() for permission in permission_classes] 
    
class SuperuserOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Tu lógica de vista aquí
        return Response({'message': 'This view is only accessible to super users.'}, status=status.HTTP_200_OK)