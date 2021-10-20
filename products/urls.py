from django.urls import path
from .views import CategoryListView, ProductDetailView

app_name = "products"

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
    path('products/', CategoryListView.as_view(), name='categories')
]
