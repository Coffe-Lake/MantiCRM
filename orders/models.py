import uuid

from django.db import models

from datetime import datetime

from phonenumber_field.modelfields import PhoneNumberField

from clients.models import *
from delivery.models import *
from marketing.models import *


class Order(models.Model):
    client_type = models.ForeignKey(
        ClientType,
        verbose_name="Имя клиента",
        on_delete=models.SET_NULL,
        null=True,
        default=''
    )
    ORDER_STATUS_CHOICES = (
        ("NEW", 'Новый'),
        ("ACCEPTED", 'Принят'),
        ("PREPARING", 'Готовится'),
        ("ORDER_READY", 'Заказ готов'),
        ("DELIVERED", 'Доставляется'),
        ("COMPLETED", 'Выполнен'),
        ("CANCELED", 'Отменен')
    )
    order_status = models.CharField(
        "Статус заказа",
        max_length=255,
        choices=ORDER_STATUS_CHOICES,
        default='Новый'
    )
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField("Телефон", unique=True, region="RU")
    address = models.CharField("Адрес", max_length=250, null=True)
    room = models.CharField("Квартира/Комната", max_length=50, blank=True, null=True)
    entrance = models.CharField("Подъезд", max_length=50, blank=True, null=True)
    floor = models.PositiveIntegerField("Этаж", blank=True, null=True)
    code = models.CharField("Код домофона", max_length=50, blank=True, null=True)
    delivery_price = models.ForeignKey(
        DeliveryPrice,
        verbose_name="Стоимость доставки",
        on_delete=models.CASCADE
    )
    discount_sum = models.ForeignKey(
        Marketing,
        verbose_name="Скидка на заказ",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    margin_order = models.PositiveIntegerField("Наценка на заказ", blank=True, null=True)
    persons = models.PositiveIntegerField("Количество персон", blank=True, null=True, default=0)
    pre_order = models.DateTimeField("Предзаказ", blank=True, null=True)
    created_at = models.DateTimeField("Создано", default=datetime.now, blank=True)
    comment = models.TextField("Комментарий", max_length=250, blank=True, null=True)
    staff_comment = models.TextField("Комментарий для повара", max_length=250, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
