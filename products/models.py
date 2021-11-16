from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# _________________ КАТЕГОРИИ ПРОДУКТОВ/ПРОДУКТЫ _________________

class Category(MPTTModel):
    available = models.BooleanField("Активный", default=0)
    title = models.CharField("Название категории", max_length=50)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    category_picture = models.ImageField("Картинка категории", blank=True)
    slug = models.SlugField("Артикул")
    created_at = models.DateTimeField("Создано", auto_now_add=True, blank=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products", kwargs={'slug': self.slug})


class Product(models.Model):
    available = models.BooleanField("Активный")
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    price = models.PositiveIntegerField("Цена", blank=True, default=0)
    composition = models.TextField("Состав", max_length=250, blank=True)
    description = models.TextField("Описание товара", max_length=250, blank=True)
    image = models.ImageField("Картинка", upload_to='products-img/', blank=True)
    slug = models.SlugField("Артикул")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products", kwargs={'slug': self.slug})
