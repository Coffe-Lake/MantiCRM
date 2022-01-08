from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list'),
    path('new_order/', NewOrderView.as_view(), name='new_order'),
    path('pre_orders/', PreOrdersListView.as_view(), name='pre_orders_list'),
    path('completed_orders/', CompletedOrdersListView.as_view(), name='completed_orders_list'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order_detail/<int:pk>/check', CheckDetailView.as_view(), name='check'),

    # ________ CRUD ________
    path('create_update_order', CreateOrder.as_view(), name='create_order'),

    # ________ AJAX ________
    path('set_status', set_status, name='set_status'),
    path('set_courier', set_courier, name='set_courier'),

]
