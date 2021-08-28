from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Curier(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField("Телефон", unique=True, region="RU")

    class Meta:
        verbose_name = "курьер"
        verbose_name_plural = "курьеры"

