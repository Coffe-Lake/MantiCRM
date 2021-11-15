from django.db import models
from django.conf import settings
from products.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)

    @classmethod
    def get_item(cls, pk):
        return cls.objects.filter(pk=pk).first()