from .models import MenuItem

ids = MenuItem.objects.values_list('id', flat=True)
print(ids)