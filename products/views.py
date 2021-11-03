from .models import *
from orders.forms import NewOrderForm
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "orders/new_order.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView,
                        self).get_context_data(**kwargs)
        # categories = Category.objects.filter(available=True) #TODO разобраться с активными продуктами
        # cat_products = Product.objects.filter(available=True)
        context["form"] = NewOrderForm
        return context


def get_queryset(self):
    return Category.objects.filter(available=True)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView,
    #                     self).get_context_data(**kwargs)
    #     product = self.get_object()
    #     context['category'] = product.category
    #     return context

    def get_queryset(self):
        return Product.objects.filter(available=True)
