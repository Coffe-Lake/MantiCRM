from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order
from orders.forms import ClientDataForm, CartForm

from django.shortcuts import render
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView


class NewOrderView(LoginRequiredMixin, View):
    """Новый заказ"""
    raise_exception = True

    @login_required()
    def get(self, request, *args, **kwargs):
        client_data_form = ClientDataForm()
        cart_form = CartForm()
        return render(request, 'orders/new_order.html', context={
            'client_form': client_data_form,
            'cart_form': cart_form,
            'title': "Новый заказ",
        })


class OrdersListView(LoginRequiredMixin, View):
    """Список заказов"""
    redirect_to_login = True

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


class PreOrdersListView(LoginRequiredMixin, View):
    """Предзаказы"""
    raise_exception = True

    def get(self, request, *args, **kwargs):
        pre_orders = Order.objects.filter(order_status="PREORDER")
        return render(request, 'orders/pre_orders_list.html', context={
            'pre_orders': pre_orders,
            'title': "Предзаказы"
        })


class CompletedOrdersListView(LoginRequiredMixin, View):
    """Завершенные"""
    raise_exception = True

    def get(self, request, *args, **kwargs):
        completed_orders = Order.objects.filter(Q(order_status="COMPLETED") |
                                                Q(order_status="CANCELED"))
        return render(request, 'orders/complete_orders_list.html', context={
            'completed_orders': completed_orders,
            'title': "Завершенные"
        })


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Детали заказа"""
    model = Order
    extra_context = {'title': "Детали заказа"}
    raise_exception = True
    #
    # def get_queryset(self):
    #     return Order.objects.all()

    # def get(self, request, pk, *args, **kwargs):
    #     orders = Order.objects.filter(id=pk)
    #     client_orders_count = Client.objects.values("phone").annotate(filter=Count(""))
    #     return render(request, 'orders/order_detail.html', context={
    #         'orders': orders,
    #         'count_client_orders': client_orders_count,
    #         'title': "Детали заказа",
    #     })

# def orders_count(request):
#     count_orders = Order.objects.exclude(
#         Q(order_status="PREORDER") |
#         Q(order_status="COMPLETED") |
#         Q(order_status="CANCELED")
#     )
#     count_pre_orders = Order.objects.filter(order_status="PREORDER")
#     count_completed_orders = Order.objects.filter(
#         Q(order_status="COMPLETED") |
#         Q(order_status="CANCELED")
#     )
#     return render(request, 'navbar.html', context={
#         'count_orders': count_orders,
#         'count_completed_orders': count_completed_orders,
#         'count_pre_orders': count_pre_orders,
#     })
