from django.contrib import admin

from .models import *


# _________________ ЗАКАЗЫ _________________

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'created_at']
    readonly_fields = ['id']
    save_on_top = True
