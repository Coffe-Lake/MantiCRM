from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.functional import cached_property


# _________________ КЛИЕНТЫ/ТИПЫ КЛИЕНТОВ _________________

class ClientType(models.Model):
    client_type = models.CharField("Тип клиента", max_length=50)
    min_orders_count = models.CharField("Мин. количество заказов",
                                        max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "тип клиента"
        verbose_name_plural = "типы клиентов"

    def __str__(self):
        return self.client_type


class Client(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField("Телефон", region="RU", unique=True)
    address = models.CharField("Адрес", max_length=250, blank=True, null=True)
    room = models.CharField("Квартира/Комната",
                            max_length=50, blank=True, null=True)
    entrance = models.CharField("Подъезд", max_length=50, blank=True, null=True)
    floor = models.PositiveIntegerField("Этаж", blank=True, null=True)
    code = models.CharField("Код домофона", max_length=50, blank=True, null=True)
    orders_count = models.PositiveIntegerField("Количество заказов", default='1', blank=True)
    client_type = models.ForeignKey(
        ClientType,
        verbose_name="Тип клиента",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return self.name
