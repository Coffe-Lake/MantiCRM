from django.contrib import admin

from .models import *


# _________________ ЗАКАЗЫ _________________

class OrderItemLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'client_data', 'order_status', 'paid', 'created_at']
    list_editable = ['order_status']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('id', 'client')
    list_filter = ('created_at', 'updated_at')
    save_on_top = True
    inlines = [OrderItemLine]
