from products.models import *
from orders.forms import OrdersForm

from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    template_name = "orders/new_order.html"
    raise_exception = True

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView,
                        self).get_context_data(**kwargs)
        context['form'] = OrdersForm
        context['title'] = "Новый заказ"
        return context

    def get_queryset(self):
        return Category.objects.filter(available=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"
    raise_exception = True

    def get_queryset(self):
        return Product.objects.filter(available=True)
