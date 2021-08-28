from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = (
    ("M", 'Муж'),
    ("F", 'Жен')
)


class Client(models.Model):
    client_name = models.CharField("Имя", max_length=50)
    client_family = models.CharField("Фамилия", max_length=50, blank=True)
    phone = PhoneNumberField(
        "Телефон",
        region='RU',
        unique=True
    )
    address = models.CharField("Адрес", max_length=200)
    email = models.EmailField("Email", blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField("Дата рождения", blank=True, null=True)
    orders_count = models.PositiveIntegerField("Количество заказов", blank=True, default=1)
    slug = models.SlugField("Метка")

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
