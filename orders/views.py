from orders.models import Order
from orders.forms import NewOrderForm

from django.shortcuts import render
from django.db.models import Count, Q
from django.views import View


class NewOrderView(View):
    """Новый заказ"""

    def get(self, request, *args, **kwargs):
        new_order_form = NewOrderForm()
        return render(request, 'orders/new_order.html', context={
            'form': new_order_form,
        })


class OrdersListView(View):
    """Список заказов"""

    def get(self, request, *args, **kwargs):
        orders = Order.objects.exclude(
            Q(order_status="PREORDER") |
            Q(order_status="COMPLETED") |
            Q(order_status="CANCELED")
        )
        return render(request, 'orders/orders_list.html', context={
            'orders': orders,
            'title': "Заказы"
        })


class PreOrdersListView(View):
    """Предзаказы"""

    def get(self, request, *args, **kwargs):
        pre_orders = Order.objects.filter(order_status="PREORDER")
        return render(request, 'orders/pre_orders_list.html', context={
            'pre_orders': pre_orders,
            'title': "Предзаказы"
        })


class CompletedOrdersListView(View):
    """Завершенные"""

    def get(self, request, *args, **kwargs):
        completed_orders = Order.objects.filter(
            Q(order_status="COMPLETED") |
            Q(order_status="CANCELED")
        )
        return render(request, 'orders/complete_orders_list.html', context={
            'completed_orders': completed_orders,
            'title': "Завершенные"
        })


def orders_count(request):
    count_orders = Order.objects.exclude(
        Q(order_status="PREORDER") |
        Q(order_status="COMPLETED") |
        Q(order_status="CANCELED")
    )
    count_pre_orders = Order.objects.filter(order_status="PREORDER")
    count_completed_orders = completed_orders = Order.objects.filter(
        Q(order_status="COMPLETED") |
        Q(order_status="CANCELED")
    )

    return render(request, 'navbar.html', context={
        'count_orders': count_orders,
        'count_completed_orders': count_completed_orders,
        'count_pre_orders': count_pre_orders,
    })


class OrderDetailView(View):
    """Детали заказа"""
    model = Order
    extra_context = {'title': 'Детали заказа'}

    def get(self, request, pk, *args, **kwargs):
        orders = Order.objects.filter(id=pk)
        count_client_orders = Order.objects.values("phone") \
            .annotate(filter=Count("phone")).order_by("phone")  # ['phone']  # ['filter'] TODO доработать код!
        return render(request, 'orders/order_detail.html', context={
            'orders': orders,
            'count_client_orders': count_client_orders,
            'title': "Детали заказа",
        })
