from clients.models import *
from delivery.models import *
from marketing.models import *
from products.models import *
from staff.models import Courier


class Order(models.Model):
    NEW = 'NEW'
    PREORDER = 'PRO'
    PREPARING = 'PRP'
    READY = 'RDY'
    DELIVERED = 'DLV'
    COMPLETED = 'COM'
    CANCELED = 'CAN'

    ORDER_STATUS_CHOICES = (
        ("NEW", 'Новый'),
        ("PREORDER", 'Предзаказ'),
        ("PREPARING", 'Готовится'),
        ("READY", 'Готов'),
        ("DELIVERED", 'Доставляется'),
        ("COMPLETED", 'Выполнен'),
        ("CANCELED", 'Отменен')
    )

    CASH = 'CAS'
    ONLINE = 'ONL'
    TERMINAL = 'TER'
    TRANSFER = 'TRN'

    PAY_METHOD_CHOICES = (
        ("CASH", 'Наличными'),
        ("ONLINE", 'Онлайн'),
        ("TERMINAL", 'Терминал'),
        ("TRANSFER", 'Переводом')
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        related_name='clients_order'
    )
    order_status = models.CharField(
        "Статус заказа",
        max_length=255,
        choices=ORDER_STATUS_CHOICES,
        default=NEW,
    )
    delivery_price = models.ForeignKey(
        DeliveryPrice,
        on_delete=models.CASCADE,
        verbose_name="Стоимость доставки",
        related_name='shipping_cost',
        default='0'
    )
    discount_sum = models.ForeignKey(
        Discounts,
        on_delete=models.CASCADE,
        verbose_name="Скидка на заказ",
        related_name='orders_discount',
        blank=True,
        null=True,
    )
    pay = models.CharField(
        "Способ оплаты",
        choices=PAY_METHOD_CHOICES,
        null=True,
        default=CASH,
        max_length=255
    )
    margin_order = models.PositiveIntegerField("Наценка на заказ", blank=True, null=True)
    persons = models.PositiveIntegerField("Количество персон",
                                          blank=True, null=True, default=0)
    pre_order = models.DateTimeField("Предзаказ", blank=True, null=True)
    mark = models.TextField("Отметка", max_length=150, blank=True, null=True)
    staff_comment = models.TextField("Комментарий для повара",
                                     max_length=150, blank=True, null=True)
    sales_channel = models.ForeignKey(
        SalesChannel,
        on_delete=models.CASCADE,
        verbose_name="Канал продаж",
        related_name='channels',
        blank=True,
        null=True,
    )
    courier = models.ForeignKey(
        Courier,
        on_delete=models.CASCADE,
        verbose_name="Курьер",
        related_name='courier',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    products = models.ForeignKey(
        Product,
        verbose_name="Продукты",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ №{self.pk}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={'pk': self.pk})

    # @cached_property
    # def order_items(self):
    #     return self.clients_order.select_related('client').all()
