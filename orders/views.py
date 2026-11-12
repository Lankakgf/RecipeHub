from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MenuItem

def menu(request):
    items = MenuItem.objects.filter(is_available=True)
    return render(request, 'orders/menu.html', {'items': items})

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id, is_available=True)
    cart = request.session.get('cart', {})
    
    item_id_str = str(item_id)
    cart[item_id_str] = cart.get(item_id_str, 0) + 1
    
    request.session['cart'] = cart
    request.session.modified = True
    messages.success(request, f"{item.name} added to cart!")
    
    return redirect(request.META.get('HTTP_REFERER', 'menu'))

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    if cart:
        menu_items = MenuItem.objects.filter(id__in=[int(k) for k in cart.keys() if k.isdigit()])
        item_map = {item.id: item for item in menu_items}

        for item_id_str, quantity in cart.items():
            if item_id_str.isdigit() and int(item_id_str) in item_map:
                item = item_map[int(item_id_str)]
                subtotal = item.price * quantity
                grand_total += subtotal
                cart_items.append({
                    'item': item,
                    'quantity': quantity,
                    'subtotal': subtotal,
                })

    return render(request, 'orders/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
    })

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    if item_id_str in cart:
        del cart[item_id_str]
        request.session['cart'] = cart
        request.session.modified = True
        messages.info(request, "Item removed from cart.")
    return redirect('cart_view')