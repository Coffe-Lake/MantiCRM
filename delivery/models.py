from django.db import models


class DeliveryPrice(models.Model):
    delivery_price = models.PositiveIntegerField('Стоимость доставки', default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = 'стоимость доставки'
        verbose_name_plural = 'стоимости доставок'
        ordering = ['delivery_price']

    def __str__(self):
        return str(self.delivery_price)
