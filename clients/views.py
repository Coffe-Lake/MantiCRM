from django.http import JsonResponse, HttpResponse

from django.shortcuts import render

from django.views import View
from .models import Client
from orders.models import Order


def validate_client(request):
    """Проверка наличия клиента по номеру телефона"""

    client_phone = request.GET.get('phone')
    print(request.GET)
    client = Client.objects.all()
    count_orders = Order.objects.filter(client_data__phone=client_phone).count()
    client_exist = client.filter(phone=client_phone).exists()

    if client_exist:
        client_data = client.get(phone=client_phone)
        response = {
            'is_taken': client_exist,
            'name': client_data.name,
            'address': client_data.address,
            'home': client_data.home,
            'building': client_data.building,
            'room': client_data.room,
            'entrance': client_data.entrance,
            'floor': client_data.floor,
            'code': client_data.code,
            'mark': client_data.mark,
            'count_orders': count_orders,
        }
        print(response)
        return JsonResponse(response)
    else:
        return HttpResponse('Клиента не существует!')
