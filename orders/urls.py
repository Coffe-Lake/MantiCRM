from django.urls import include, path

from rest_framework import routers

from .views import index, about

# OrderViewSet
# router = routers.DefaultRouter()
# router.register(r'orders', OrderViewSet)
#
# app_name = "orders"

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', index, name='home'),
    path('about/', about, name='about'),
]
