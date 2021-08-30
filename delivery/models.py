from django.db import models


class DeliveryPrice(models.Model):
    delivery_price = models.PositiveIntegerField('Стоимость доставки', default=0)

    class Meta:
        verbose_name = 'стоимость доставки'
        verbose_name_plural = 'стоимости доставок'

    def __str__(self):
        return str(self.delivery_price)


# class DeliveryMethod(models.Model):
#     delivery_method = models.CharField('Способ доставки', max_length=50)
#
#     class Meta:
#         verbose_name = 'способ доставки'
#         verbose_name_plural = 'способы доставок'
