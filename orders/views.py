from django.shortcuts import render

from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render, get_object_or_404

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('-created_at')
#     serializer_class = OrderSerializer


fields = Order.objects.all()


def index(request):
    return render(
        request,
        'orders/index.html',
        {
            'fields': fields,
            'title': 'Главная страница'
        }
    )


def about(request):
    return render(request, 'orders/about.html', {'title': 'О сайте'})
