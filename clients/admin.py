from django.contrib import admin

from .models import *


# _________________ КЛИЕНТЫ _________________


@admin.register(Client)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'phone', 'address', 'email', 'orders_count', 'id']
    # list_editable = ['phone', 'address', 'email', 'gender']
