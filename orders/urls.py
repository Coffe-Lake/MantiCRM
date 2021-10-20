from django.urls import include, path

from .views import OrderDetailView, OrderListView, NewOrderView

urlpatterns = [
    path('new_order/', NewOrderView.as_view(), name='new_order'),
    path('orders_list/', OrderListView.as_view(), name='orders_list'),
    path('orders_list/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
