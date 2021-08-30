from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# _________________ КЛИЕНТЫ/ТИПЫ КЛИЕНТОВ _________________

class ClientType(models.Model):
    client_type = models.CharField("Тип клиента", max_length=50)
    orders_count = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'тип клиента'
        verbose_name_plural = 'типы клиентов'

    def __str__(self):
        return self.client_type


class Client(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = PhoneNumberField(
        "Телефон",
        region='RU',
        unique=True
    )
    phone_2 = PhoneNumberField(
        "Доп.Телефон",
        region='RU',
        blank=True,
        null=True
    )
    address = models.CharField("Адрес", max_length=200)
    email = models.EmailField("Email", blank=True)
    GENDER_CHOICES = (
        ("M", 'Муж'),
        ("F", 'Жен')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField("Дата рождения", blank=True, null=True)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, null=True)
    orders_count = models.PositiveIntegerField("Количество заказов", blank=True, default=0)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return self.name
