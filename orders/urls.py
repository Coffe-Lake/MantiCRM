from django.urls import path

from .views import *
from products.views import CategoryListView

urlpatterns = [
    path('new_order/', CategoryListView.as_view(), name='new_order'),
    path('', OrdersListView.as_view(), name='orders_list'),
    path('pre_orders/', PreOrdersListView.as_view(), name='pre_orders_list'),
    path('completed_orders/', CompletedOrdersListView.as_view(), name='completed_orders_list'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
