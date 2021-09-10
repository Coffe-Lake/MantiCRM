from django.contrib import admin

from .models import *


# _________________ ЗАКАЗЫ _________________

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'phone', 'address', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    save_on_top = True
