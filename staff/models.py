from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Courier(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField("Телефон", region="RU", blank=True, )

    class Meta:
        verbose_name = "курьер"
        verbose_name_plural = "курьеры"

    def __str__(self):
        return self.name
