from django.db import models

AVAILABLE_CHOICES = (
    ("are_available", 'В наличии'),
    ("not_available", 'Нет в наличии')
)


# _________________ КАТЕГОРИИ ПРОДУКТОВ/ПРОДУКТЫ _________________

class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)
    # description = models.CharField("Описание категории", max_length=100)
    category_picture = models.ImageField("Картинка категории", blank=True)
    slug = models.SlugField("Артикул")
    created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    available = models.BooleanField("В наличии", default=0)
    # available = models.CharField(
    #     "Наличие",
    #     choices=AVAILABLE_CHOICES,
    #     default=AVAILABLE_CHOICES[0][1],
    #     max_length=255
    # )
    name = models.CharField("Название", max_length=50)
    price = models.PositiveIntegerField("Цена", blank=True, default=0)
    composition = models.TextField("Состав", max_length=250)
    description = models.TextField("Описание товара", max_length=250)
    image = models.ImageField("Картинка", upload_to='products-img/', blank=True)
    slug = models.SlugField("Артикул")
    created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name
