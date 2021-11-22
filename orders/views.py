from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Order
from clients.models import Client
from orders.forms import OrdersForm

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView


class NewOrderView(LoginRequiredMixin, View):
    """Новый заказ"""
    raise_exception = True

    @login_required()
    def get(self, request, *args, **kwargs):
        return render(request, 'orders/new_order.html', context={
            'title': "Новый заказ",
        })


class OrdersListView(LoginRequiredMixin, View):
    """Список заказов"""
    redirect_to_login = True

    def get(self, request, *args, **kwargs):
        orders = Order.objects.exclude(
            Q(order_status="PRO") |
            Q(order_status="COM") |
            Q(order_status="CAN")
        )
        return render(request, 'orders/orders_list.html', context={
            'orders': orders,
            'title': "Заказы"
        })


class PreOrdersListView(LoginRequiredMixin, View):
    """Предзаказы"""
    raise_exception = True

    def get(self, request, *args, **kwargs):
        pre_orders = Order.objects.filter(order_status="PRO")
        return render(request, 'orders/pre_orders_list.html', context={
            'pre_orders': pre_orders,
            'title': "Предзаказы"
        })


class CompletedOrdersListView(LoginRequiredMixin, View):
    """Завершенные"""
    raise_exception = True

    def get(self, request, *args, **kwargs):
        completed_orders = Order.objects.filter(Q(order_status="COM") |
                                                Q(order_status="CAN"))
        return render(request, 'orders/complete_orders_list.html', context={
            'completed_orders': completed_orders,
            'title': "Завершенные"
        })


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Детали заказа"""
    model = Order
    extra_context = {'title': "Детали заказа"}
    raise_exception = True
    success_url = reverse_lazy('order_detail')


def createOrder(request):
    form = OrdersForm()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'orders/new_order.html', context={
        'form': form,
    })
