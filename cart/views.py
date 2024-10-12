from decimal import Decimal
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from info.models import Info
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # Ensure this line is correct
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Get quantity from the form
    cart.add(product=product, quantity=quantity, override_quantity=True)  # This should work if add is defined
    return redirect('cart:cart_detail')



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    count = Decimal('0.02')  # Convert the float to Decimal
    discount = Decimal(cart.get_total_price()) * count
    delivery = Decimal('0.05') * Decimal(cart.get_total_price())
    subtotal = cart.get_total_price()
    total_price = subtotal - discount + delivery
    info = Info.objects.all()
    products = Product.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
        # Debugging line to check product id
    total_price = cart.get_total_price()
    return render(request, 'landing/cart.html', context ={
        'cart': cart,
        'total_price': total_price,
        "products": products,
        "info": info,
        'discount': discount,
        'delivery': delivery,
        'total_price': total_price,
        })

