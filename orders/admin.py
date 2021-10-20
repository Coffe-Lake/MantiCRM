from django.contrib import admin

from .models import *
from products.models import Product


# _________________ ЗАКАЗЫ _________________

# class OrderInline(admin.TabularInline):
#     model = Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'phone', 'address', 'created_at']
    readonly_fields = ['orders_count', 'created_at', 'updated_at']
    search_fields = ('id', 'name', 'phone', 'address')
    list_filter = ('created_at', 'updated_at')
    save_on_top = True
    # inlines = [
    #     OrderInline,
    # ]
