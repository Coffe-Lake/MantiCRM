import uuid

from django.db import models

from datetime import datetime

from phonenumber_field.modelfields import PhoneNumberField

ORDER_STATUS_CHOICES = (
    ("NEW", 'Новый'),
    ("ACCEPTED", 'Принят'),
    ("PREPARING", 'Готовится'),
    ("ORDER_IS_READY", 'Заказ готов'),
    ("DELIVERED", 'Доставляется'),
    ("COMPLETED", 'Выполнен'),
    ("CANCELED", 'Отменен')
)


class Order(models.Model):
    order_status = models.CharField(
        "Статус заказа",
        max_length=255,
        choices=ORDER_STATUS_CHOICES,
        default='Новый'
    )
    client_name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField("Телефон", unique=True, region="RU")
    address = models.CharField("Адрес", max_length=250, null=True)
    room = models.CharField("Квартира/Комната", max_length=50, blank=True, null=True)
    entrance = models.CharField("Подъезд", max_length=50, blank=True, null=True)
    floor = models.PositiveIntegerField("Этаж", blank=True, null=True)
    code = models.CharField("Код домофона", max_length=50, blank=True, null=True)
    delivery_price = models.PositiveIntegerField("Стоимость доставки", blank=True, null=True, default=0)
    discount_sum = models.PositiveIntegerField("Скидка на заказ", blank=True, null=True)
    margin_order = models.PositiveIntegerField("Наценка на заказ", blank=True, null=True)
    persons = models.PositiveIntegerField("Количество персон", blank=True, null=True, default=0)
    pre_order = models.DateTimeField("Предзаказ", blank=True, null=True)
    created_at = models.DateTimeField("Создано", default=datetime.now, blank=True)
    comment = models.TextField("Комментарий", max_length=250, blank=True, null=True)
    staff_comment = models.TextField("Комментарий для повара", max_length=250, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=6)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
