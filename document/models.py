# from django.db import models
#
#
# class Invoice(models.Model):
#     organization_title = models.CharField('Название предприятия', blank=True, max_length=255)
#     inn = models.CharField('ИНН', max_length=12, blank=True)
#     payment_check = models.CharField('Рассч. счет', max_length=20, blank=True)
#     corr_check = models.CharField('Корр. счет', max_length=20, blank=True)
#     bik = models.CharField('БИК', max_length=11, blank=True)
#     organization_address = models.CharField('Адрес предприятия', max_length=255, blank=True)
#     organization_phone = models.CharField('Телефон предприятия', max_length=255, blank=True)
#     organization_email = models.CharField('Почта предприятия', max_length=255, blank=True)
#     organization_site = models.CharField('Сайт предприятия', max_length=255, blank=True)
#     create_at = models.DateTimeField('Создано', auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField('Обновлено', auto_now=True, blank=True)
#
#     class Meta:
#         verbose_name = "накладная"
#         verbose_name_plural = "накладные"
#         abstract = True
#
#     def __str__(self):
#         return str(self.organization_title)
