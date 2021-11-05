from django.urls import path, include

from .views import OrderDetailView, OrderListView, NewOrderView
from products.views import CategoryListView

urlpatterns = [
    path('new_order/', CategoryListView.as_view(), name='new_order'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('orders_list/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
