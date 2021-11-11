from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from orders.models import Order


# from orders.models import Order


# _________________ КЛИЕНТЫ/ТИПЫ КЛИЕНТОВ _________________

class ClientType(models.Model):
    client_type = models.CharField("Тип клиента", max_length=50)
    min_orders_count = models.CharField("Мин. количество заказов",
                                        max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'тип клиента'
        verbose_name_plural = 'типы клиентов'

    def __str__(self):
        return self.client_type


class Client(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField(
        "Телефон",
        region='RU',
        unique=True
    )
    address = models.CharField("Адрес", max_length=200)
    email = models.EmailField("Email", blank=True, null=True)
    birthday = models.DateField("Дата рождения", blank=True, null=True)
    orders_count = models.PositiveIntegerField("Количество заказов", blank=True, default=0)
    client_type = models.ForeignKey(
        ClientType,
        verbose_name='Тип клиента',
        on_delete=models.SET_NULL,
        default="Новый",
        null=True
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    customer_orders = models.ForeignKey(Order, verbose_name="Заказы клиента", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return self.name
