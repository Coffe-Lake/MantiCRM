from .models import *
from django.views.generic import View, ListView, DetailView


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "products/products_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView,
                        self).get_context_data(**kwargs)
        context['title'] = 'Продукты'
        product = Category.objects.filter(available=True)
        category_slug = self.kwargs.get('slug')
        # context['product'] = product.get_children.filter(available=True)
        if category_slug:
            category = Category.objects.all()
            context['product'] = category.p_category_set.filter(available=True)
            return context
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
