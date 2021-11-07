from django.urls import path
from .views import ProductDetailView

app_name = "products"

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
]
