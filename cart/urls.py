from .views import cart
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', cart.index, name='index'),
]