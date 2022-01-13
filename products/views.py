from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm
from products.models import *
from orders.models import Order
from orders.forms import OrderForm, ClientForm

from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


# class CategoryListView(LoginRequiredMixin, ListView):
#     model = Category
#     context_object_name = "categories"
#     template_name = "orders/new_order.html"
#     raise_exception = True
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(CategoryListView,
#                         self).get_context_data(**kwargs)
#         return context
#
#     def get_queryset(self):
#         return Category.objects.filter(available=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"
    raise_exception = True

    def get_queryset(self):
        return Product.objects.filter(available=True)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "products/product_detail.html", {'product': product,
                                                        'cart_product_form': cart_product_form})
