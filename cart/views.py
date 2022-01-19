from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cart.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@login_required
def cart_add(request):
    product_id = request.POST.get('product')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned = form.cleaned_data
        cart.add(product=product,
                 quantity=cleaned['quantity'],
                 update_quantity=cleaned['update'])
        return HttpResponse(status=200)
    return True


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponse(status=200)


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_section.html', {'cart': cart})
