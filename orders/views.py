from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order
from clients.models import Client
from orders.forms import NewOrderForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('-created_at')
#     serializer_class = OrderSerializer

# fields = Order.objects.all()

from django.views import View


class NewOrderView(View):
    def get(self, request, *args, **kwargs):
        new_order_form = NewOrderForm()
        return render(request, 'orders/new_order.html', context={
            "form": new_order_form,
            "title": "Новый заказ"
        })


class OrderListView(View):
    """Список заказов"""
    model = Order

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        return render(request, 'orders/orders_list.html', context={
            "orders": orders,
            "title": "Заказы"
        })


class OrderDetailView(View):
    """Детали заказа"""
    model = Order
    template_name = "orders/order_detail.html"
    extra_context = {'title': 'Детали заказа'}

    def get(self, request, pk, *args, **kwargs):
        orders = Order.objects.filter(id=pk)
        return render(request, 'orders/order_detail.html', context={
            'orders': orders,
            "title": "Детали заказа"
        })


class AddClient(View):
    """Клиент"""

    def post(self, request, pk):
        form = ClientForm(request.POST)
        client = Client.objects.create(form)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = client
            form.save()
        return redirect(client.get_absolute_url())
