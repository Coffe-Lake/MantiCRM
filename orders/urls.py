from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list'),
    path('pre_orders/', PreOrdersListView.as_view(), name='pre_orders_list'),
    path('completed_orders/', CompletedOrdersListView.as_view(), name='completed_orders_list'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order_detail/<int:pk>/check', CheckDetailView.as_view(), name='check'),
    # path('order_update/<int:pk>/update', OrderUpdateView.as_view(), name='update_order'),

    # ________ CRUD ________
    path('create_order', CreateOrder.as_view(), name='create_order'),
]
