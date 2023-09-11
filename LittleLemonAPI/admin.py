from django.contrib import admin
from . import models
from .models import MenuItem
# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'featured', 'category')

# Registrar el modelo con la clase personalizada en el administrador
admin.site.register(MenuItem, MenuItemAdmin)