from products.models import *
from orders.forms import NewOrderForm

from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "orders/new_order.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView,
                        self).get_context_data(**kwargs)
        context['form'] = NewOrderForm
        context['title'] = "Новый заказ"
        return context

    def get_queryset(self):
        return Category.objects.filter(available=True)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(available=True)
