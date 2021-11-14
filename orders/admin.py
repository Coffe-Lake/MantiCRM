from django.contrib import admin

from .models import *
from products.models import Product


# _________________ ЗАКАЗЫ _________________

# class OrderInline(admin.TabularInline):
#     model = Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'client', 'order_status', 'created_at']
    list_editable = ['order_status']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('id', 'client')
    list_filter = ('created_at', 'updated_at')
    save_on_top = True
    # inlines = [
    #     OrderInline,
    # ]
