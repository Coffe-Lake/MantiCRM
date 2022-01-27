from django.apps import AppConfig


class DocumentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'document'
    verbose_name = 'документ'
    verbose_name_plural = 'документы'
