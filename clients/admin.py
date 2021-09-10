from django.contrib import admin

from .models import *


# _________________ КЛИЕНТЫ _________________


@admin.register(Client)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'email', 'orders_count', 'id']
    readonly_fields = ['created_at', 'orders_count', 'id']
    # list_editable = ['phone', 'address', 'email', 'gender']


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ['client_type', 'id']
    readonly_fields = ['id']
