from rest_framework.permissions import IsAuthenticated, IsAdminUser

#Mixin que aplica IsAuthenticated e IsAdminUser como clases de permisos cuando el método de la solicitud no es 'GET',
class PermissionMixin:
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated, IsAdminUser]
        return[permission() for permission in permission_classes] 