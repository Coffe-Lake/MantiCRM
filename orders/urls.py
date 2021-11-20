from django.urls import path

from .views import *
from products.views import CategoryListView

app_name = 'orders'

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list'),
    path('new_order/', CategoryListView.as_view(), name='new_order'),
    path('pre_orders/', PreOrdersListView.as_view(), name='pre_orders_list'),
    path('completed_orders/', CompletedOrdersListView.as_view(), name='completed_orders_list'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    path('create_order/', createOrder, name='create_order'),
    path('add/', addpage, name='create_order')
]
