from datetime import timedelta
from pprint import pprint

from django.forms import inlineformset_factory
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from orders.forms import *

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView, UpdateView

from products.models import Category
from .models import Order, OrderItem


# class NewOrderView(View):
#     """Новый заказ"""
#
#     redirect_to_login = True


class CreateOrderView(LoginRequiredMixin, View):
    """Форма создания заказа"""

    raise_exception = True

    def get(self, request, *args, **kwargs):
        new_order_pk = Order.objects.first()
        if new_order_pk is None:
            new_order_pk = 'Заказ №1'
        else:
            new_order_pk = f'Заказ №{Order.objects.first().id + 1}'
        # Номер нового заказа

        context = {
            'categories': Category.objects.filter(available=True),
            'form_client': ClientForm,
            'form_order': OrderForm,
            'new_order_pk': new_order_pk,
            'title': "Новый заказ"
        }
        return render(request, 'orders/new_order.html', context)

    def post(self, request):
        form_client = ClientForm(request.POST)
        form_order = OrderForm(request.POST)
        pprint(request.POST)
        if form_client.is_valid() and form_order.is_valid():
            # Валидация формы клиента и заказа
            client_instance = form_client.save(commit=False)
            # Экземпляр клиента
            update_values = {
                'name': form_client.cleaned_data['name'],
                'address': form_client.cleaned_data['address'],
                'home': form_client.cleaned_data['home'],
                'building': form_client.cleaned_data['building'],
                'room': form_client.cleaned_data['room'],
                'entrance': form_client.cleaned_data['entrance'],
                'floor': form_client.cleaned_data['floor'],
                'code': form_client.cleaned_data['code'],
                'mark': form_client.cleaned_data['mark'],
            }
            # Словарь данных из формы
            update_client, created = Client.objects.update_or_create(
                phone=client_instance.phone,
                defaults=update_values
            )
            # Создать или обновить данные клиента
            if created:
                print(f"Клиент {update_client} создан ")
            else:
                print(f"Данные {update_client} обновлены")
            # Показать статус добавления клиента в запросах
            update_client.save()
            # Сохраняем клиента перед сохранением заказа, для передачи заказу id клиента
            client_pk = Client.objects.get(phone=client_instance.phone).id
            # Возвращаем из БД "ID" клиента
            order_instance = form_order.save(commit=False)
            # Экземпляр заказа
            order_instance.operator = request.user
            # Сохраняем в экземпляр оператора создавшего заказ
            order_instance.client_data_id = client_pk
            # Присваиваем клиенту заказ по client_id
            form_order.save()
            # Сохраняем заказа
        return redirect('orders:orders_list')
        # TODO доработать формсет, добавить корзину


class UpdateOrderView(LoginRequiredMixin, View):
    redirect_to_login = True

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, id=pk)
        context = {}
        if request.method == 'POST':
            form_client = ClientForm(request.POST)
            form_order = OrderForm(request.POST)
            pprint(request.POST)
            if form_client.is_valid() and form_order.is_valid():
                # Валидация формы клиента и заказа
                client_instance = form_client.save(commit=False)
                # Экземпляр клиента
                update_values = {
                    'name': form_client.cleaned_data['name'],
                    'address': form_client.cleaned_data['address'],
                    'home': form_client.cleaned_data['home'],
                    'building': form_client.cleaned_data['building'],
                    'room': form_client.cleaned_data['room'],
                    'entrance': form_client.cleaned_data['entrance'],
                    'floor': form_client.cleaned_data['floor'],
                    'code': form_client.cleaned_data['code'],
                    'mark': form_client.cleaned_data['mark'],
                }
                # Словарь данных из формы
                update_client, created = Client.objects.update_or_create(
                    phone=client_instance.phone,
                    defaults=update_values
                )
                # Создать или обновить данные клиента
                if created:
                    print(f"Клиент {update_client} создан ")
                else:
                    print(f"Данные {update_client} обновлены")
                # Показать статус добавления клиента в запросах
                update_client.save()
                # Сохраняем клиента перед сохранением заказа, для передачи заказу id клиента
                client_pk = Client.objects.get(phone=client_instance.phone).id
                # Возвращаем из БД "ID" клиента
                order_instance = form_order.save(commit=False)
                # Экземпляр заказа
                order_instance.operator = request.user
                # Сохраняем в экземпляр оператора создавшего заказ
                order_instance.client_data_id = client_pk
                # Присваиваем клиенту заказ по client_id
                form_order.save()
                # Сохраняем заказа
            return redirect('orders:orders_list')
        else:
            context = {
                'categories': Category.objects.filter(available=True),
                'form_client': ClientForm(instance=order.client_data),
                'form_order': OrderForm(instance=order),
                'order': order,
                'title': "Изменить заказ"
            }
        return render(request, 'orders/order_update.html', context)

    # def post(self, request, *args, **kwargs):


# model = Order
# form_class = OrderForm
# success_url = reverse_lazy('orders:update_order')
#
# def get_context_data(self, **kwargs):  # формирование formset
#     data = super().get_context_data(**kwargs)
#     OrderFormSet = inlineformset_factory(
#         Order, OrderItem, form=OrderForm, extra=1
#     )
#     if self.request.POST:
#         formset = OrderFormSet(
#             self.request.POST, self.request.FILES,
#             instance=self.object
#         )
#     else:
#         queryset = self.object.orderitems.select_related()
#         formset = OrderFormSet(instance=self.object, queryset=queryset)
#         for form in formset.forms:
#             if form.instance.pk:
#                 form.initial['price'] = form.instance.product.price
#         data['orderitems'] = formset
#     data['orderitems'] = formset
#     return data
#
# def form_valid(self, form):  # проверяет и сохраняет форму
#     context = self.get_context_data()
#     orderitems = context['orderitems']
#
#     with transaction.atomic():
#         self.object = form.save()
#         if orderitems.is_valid():
#             orderitems.instance = self.object
#             orderitems.save()
#
#     return super().form_valid(form)


class OrdersListView(LoginRequiredMixin, View):
    """Список заказов в работе"""

    redirect_to_login = True

    def get(self, request, *args, **kwargs):
        orders = Order.objects.exclude(
            Q(pre_order__gt=timezone.now() + timedelta(hours=2)) |
            Q(order_status="COM") |
            Q(order_status="CAN")
        )
        # Вывести все заказы и предзаказы за 2 часа до доставки
        return render(request, 'orders/orders_list.html', context={
            'orders': orders,
            'form_status': OrderCourierForm(),
            'title': "Заказы"
        })

    def post(self, request, *args, **kwargs):
        updated_order_status = request.POST.get('order_status')
        order_id = request.POST.get('order_id')
        print(request.POST)
        order = Order.objects.get(id=order_id)
        order.order_status = updated_order_status
        order.save()
        return HttpResponse(status=200)


class PreOrdersListView(LoginRequiredMixin, View):
    """Список предзаказов"""

    redirect_to_login = True

    def get(self, request, *args, **kwargs):
        current_time = timezone.localtime()
        before_time_preparing = current_time + timedelta(hours=2)
        pre_orders = Order.objects.filter(
            Q(pre_order__gt=before_time_preparing)
        )
        # Перенести в предзаказы, время до доставки более 2х часов
        for item in pre_orders:
            if item.pre_order > before_time_preparing:
                pre_orders.update(order_status="PRO")
        # Поменять статус заказа на предзаказ

        return render(request, 'orders/pre_orders_list.html', context={
            'pre_orders': pre_orders,
            'form_status': OrderCourierForm(),
            'title': "Предзаказы"
        })


class CompletedOrdersListView(LoginRequiredMixin, View):
    """Список завершенных заказов"""

    redirect_to_login = True

    def get(self, request, *args, **kwargs):
        completed_orders = Order.objects.filter(Q(order_status="COM") |
                                                Q(order_status="CAN"))
        # Фильтровать отмененные и завершенные заказы
        return render(request, 'orders/complete_orders_list.html', context={
            'completed_orders': completed_orders,
            'form_status': OrderCourierForm(),
            'title': "Завершенные"
        })


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Детали заказа"""

    model = Order
    extra_context = {'title': "Детали заказа"}
    redirect_to_login = True
    success_url = reverse_lazy('order_detail')


class CheckDetailView(LoginRequiredMixin, DetailView):
    """Чек"""

    model = Order
    template_name = 'orders/invoice/check.html'
    extra_context = {'title': "Печать чека"}
    redirect_to_login = True
    success_url = reverse_lazy('check')
