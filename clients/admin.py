from django.contrib import admin

from .models import *


# _________________ КЛИЕНТЫ _________________


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'orders_count', 'id']
    readonly_fields = ['orders_count', 'created_at', 'id']
    search_fields = ['name', 'phone', 'orders_count', 'address']
    list_filter = ('created_at', 'updated_at')
    # list_editable = ['phone', 'address', 'email', 'gender']


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ['client_type', 'id']
    readonly_fields = ['id']
