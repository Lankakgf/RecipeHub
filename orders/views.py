from django.shortcuts import render
from .models import MenuItem

def menu(request):
    items = MenuItem.objects.filter(is_available=True)
    return render(request, 'orders/menu.html', {'items': items})