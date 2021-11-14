from django.db import models


# _________________ СКИДКИ/АКЦИИ/КУПОНЫ _________________

class Discounts(models.Model):
    DISCOUNT_CHOICES = (
        ('SUM', 'Сумма'),
        ('PERCENT', 'Процент от суммы')
    )
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=100, blank=True)
    discount_type = models.CharField('Вид скидки', max_length=255, choices=DISCOUNT_CHOICES, blank=True)
    discount = models.PositiveIntegerField('Скидка', default=0)
    coupon = models.CharField('Промокод', max_length=10, blank=True)
    create_ad = models.DateTimeField('Создано', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "скидки и акции"
        verbose_name_plural = "скидки и акции"

    def __str__(self):
        return str(self.name)


# _________________ КАНАЛЫ ПРОДАЖ _________________

class SalesChannel(models.Model):
    title = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = "канал продаж"
        verbose_name_plural = "каналы продаж"

    def __str__(self):
        return self.title
