from django.contrib import admin

from .models import *


@admin.register(DeliveryPrice)
class DeliveryPriceAdmin(admin.ModelAdmin):
    list_display = ['delivery_price']


@admin.register(PayMethod)
class PayMethodAdmin(admin.ModelAdmin):
    list_display = ['pay_method']


# @admin.register(DeliveryMethod)
# class DeliveryMethodAdmin(admin.ModelAdmin):
#     list_display = ['delivery_method']
