from django.db import models


# _________________ СКИДКИ/АКЦИИ/КУПОНЫ _________________

class Marketing(models.Model):
    DISCOUNT_CHOICES = (
        ('1', 'Сумма'),
        ('2', 'Процент от суммы')
    )
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=100, blank=True)
    discount_type = models.CharField('Вид скидки', max_length=1, choices=DISCOUNT_CHOICES, blank=True)
    discount = models.PositiveIntegerField('Скидка', default=0)

    class Meta:
        verbose_name = "маркетинг"
        verbose_name_plural = "маркетинг"

    def __str__(self):
        return str(self.name)