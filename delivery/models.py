from django.db import models


# class DeliveryPrice(models.Model):
#     delivery_price = models.PositiveIntegerField('Стоимость доставки', default=0)
#     created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField("Обновлено", auto_now=True)
#
#     class Meta:
#         verbose_name = 'стоимость доставки'
#         verbose_name_plural = 'стоимости доставок'
#         ordering = ['delivery_price']
#
#     def __str__(self):
#         return str(self.delivery_price)


# class PayMethod(models.Model):
#     pay_method = models.CharField("Способ оплаты",
#                                   max_length=100, db_index=True)
#     created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField("Обновлено", auto_now=True)
#
#     class Meta:
#         verbose_name = "способ оплаты"
#         verbose_name_plural = "способы оплаты"
#         ordering = ['pay_method']
#
#     def __str__(self):
#         return self.pay_method

# class DeliveryMethod(models.Model):
#     delivery_method = models.CharField('Способ доставки', max_length=50)
#
#     class Meta:
#         verbose_name = 'способ доставки'
#         verbose_name_plural = 'способы доставок'
