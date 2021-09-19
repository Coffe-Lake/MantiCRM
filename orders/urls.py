from django.urls import include, path

from rest_framework import routers

from .views import OrderDetailView, OrderListView, NewOrderView

# OrderViewSet
# router = routers.DefaultRouter()
# router.register(r'orders', OrderViewSet)
#
# app_name = "orders"

urlpatterns = [
    # path('api/', include(router.urls)),
    path('new_order/', NewOrderView.as_view(), name='new_order'),
    path('orders_list/', OrderListView.as_view(), name='orders_list'),
    path('orders_list/details/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]
