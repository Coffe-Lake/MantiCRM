from pprint import pprint
import phonenumbers

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from orders.forms import *

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView, ListView


class NewOrderView(LoginRequiredMixin, View):
    """Новый заказ"""
    raise_exception = True

    def post(self, request):
        form_client = ClientForm(request.POST)
        form_order = OrderForm(request.POST)
        pprint(request.POST)
        if form_client.is_valid() and form_order.is_valid():  # Валидация формы клиента и заказа
            client_instance = form_client.save(commit=False)  # Экземпляр клиента
            update_values = {
                'name': form_client.cleaned_data['name'],
                'address': form_client.cleaned_data['address'],
                'home': form_client.cleaned_data['home'],
                'building': form_client.cleaned_data['building'],
                'room': form_client.cleaned_data['room'],
                'entrance': form_client.cleaned_data['entrance'],
                'floor': form_client.cleaned_data['floor'],
                'code': form_client.cleaned_data['code'],
            }
            update_client, created = Client.objects.update_or_create(
                phone=client_instance.phone,
                defaults=update_values
            )  # Создание и обновление клиента
            if created:
                print(f"Клиент {update_client} создан ")
            else:
                print(f"Клиент {update_client} обновлен")
            update_client.save()  # Сохраняем клиента перед сохранением заказа для передачи ему id клиента

            client_pk = Client.objects.get(phone=client_instance.phone).id  # Возвращаем из БД "ID" клиента
            order_instance = form_order.save(commit=False)  # Экземпляр заказа
            order_instance.operator = request.user  # Сохраняем в экземпляр оператора, юзера создавшего заказ
            order_instance.client_data_id = client_pk  # Присваиваем заказ клиенту по id клиента
            form_order.save()  # Сохраняем заказа
        return redirect('orders:orders_list')


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
