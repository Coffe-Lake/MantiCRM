from .models import Order
from orders.forms import NewOrderForm
from django.shortcuts import render
from django.db.models import Count
from django.views import View


class NewOrderView(View):
    """Новый заказ"""

    def get(self, request, *args, **kwargs):
        new_order_form = NewOrderForm()
        return render(request, 'orders/new_order.html', context={
            "form": new_order_form,
            "title": "Новый заказ"
        })


class OrderListView(View):
    """Список заказов"""

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
        count_orders = Order.objects.values("phone") \
            .annotate(filter=Count("phone")).order_by("phone")  # ['phone']  # ['filter'] TODO доработать код!
        return render(request, 'orders/order_detail.html', context={
            'orders': orders,
            'count_orders': count_orders,
            "title": "Детали заказа",
        })

# TODO Код ниже перенести в clients и доработать
# class AddClient(View):
#     """Добавить клиент"""
#
#     def post(self, request, pk):
#         form = NewOrderForm(request.POST)
#         client = Client.objects.create(form)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.client = client
#             form.save()
#         return redirect(client.get_absolute_url())
