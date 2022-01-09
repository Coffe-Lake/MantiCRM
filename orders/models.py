from django.contrib.auth.models import User

from django.db import models


from clients.models import *
from delivery.models import *
from marketing.models import *
from products.models import *
from staff.models import *


class Order(models.Model):
    NEW = 'NEW'
    PREORDER = 'PRO'
    PREPARING = 'PRP'
    READY = 'RDY'
    DELIVERED = 'DLV'
    COMPLETED = 'COM'
    CANCELED = 'CAN'

    ORDER_STATUS_CHOICES = (
        (NEW, 'Новый'),
        (PREORDER, 'Предзаказ'),
        (PREPARING, 'Готовится'),
        (READY, 'Готов'),
        (DELIVERED, 'Доставляется'),
        (COMPLETED, 'Выполнен'),
        (CANCELED, 'Отменен')
    )

    CASH = 'CAS'
    ONLINE = 'ONL'
    TERMINAL = 'TER'
    TRANSFER = 'TRN'

    PAY_METHOD_CHOICES = (
        (CASH, 'Наличными'),
        (ONLINE, 'Онлайн'),
        (TERMINAL, 'Терминал'),
        (TRANSFER, 'Переводом')
    )

    client_data = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        verbose_name="Клиент",
        related_name="c_order",
        blank=True,
        null=True,
    )
    order_status = models.CharField(
        "Статус заказа",
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=NEW,
        blank=True,
        null=True,
    )
    delivery_price = models.ForeignKey(
        DeliveryPrice,
        on_delete=models.SET_NULL,
        verbose_name="Стоимость доставки",
        related_name="shipping_cost",
        blank=True,
        null=True,
    )
    discount_sum = models.ForeignKey(
        Discounts,
        on_delete=models.SET_NULL,
        verbose_name="Скидка на заказ",
        related_name="orders_discount",
        blank=True,
        null=True,
    )
    pay_method = models.CharField(
        "Способ оплаты",
        choices=PAY_METHOD_CHOICES,
        default=CASH,
        max_length=3,
        blank=True,
        null=True,
    )
    paid = models.BooleanField(verbose_name="Оплачено", default=False)
    persons = models.PositiveIntegerField("Количество персон",
                                          blank=True, null=True, default=0)
    pre_order = models.DateTimeField("Доставить", blank=True, null=True)
    staff_comment = models.TextField("Комментарий для повара",
                                     max_length=150, blank=True, null=True)
    sales_channel = models.ForeignKey(
        SalesChannel,
        on_delete=models.SET_NULL,
        verbose_name="Канал продаж",
        related_name="channels",
        blank=True,
        null=True,
    )
    courier = models.ForeignKey(
        Courier,
        on_delete=models.CASCADE,
        verbose_name="Курьер",
        related_name="courier",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    operator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Оператор",
    )

    # order_pk = models.AutoField(primary_key=True, db_index=True)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ №{self.pk}"

    # def get_absolute_url(self):
    #     return reverse("order_detail", kwargs={'pk': self.pk})
    #
    # @cached_property
    # def is_new(self):
    #     return self.order_status == self.NEW
    #
    # @cached_property
    # def order_items(self):
    #     return self.order_items.select_related('product').all()
    #
    # @cached_property
    # def total_quantity(self):
    #     return sum(list(map(lambda x: x.quantity, self.order_items)))
    #
    # @cached_property
    # def total_cost(self):
    #     return sum(list(map(lambda x: x.quantity * x.product.price, self.order_items)))
    #
    # @property
    # def summary(self):
    #     items = self.order_items.select_related('product').all()
    #     return {
    #         "total_cost": sum(list(map(lambda x: x.quantity * x.product.price, items))),
    #         "total_quantity": sum(list(map(lambda x: x.quantity, self.order_items)))
    #     }
    #


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Заказ",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name="Продукт",
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=1,
        blank=True,
        null=True,
    )
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    # @cached_property
    # def get_cost(self):
    #     return self.product.price * self.quantity
    #
    # @classmethod
    # def get_item(cls, pk):
    #     return cls.objects.filter(pk=pk).first()
