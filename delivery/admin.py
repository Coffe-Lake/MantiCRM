from django.contrib import admin

from .models import *


# @admin.register(DeliveryPrice)
# class DeliveryPriceAdmin(admin.ModelAdmin):
#     list_display = ['delivery_price', 'id']
#     readonly_fields = ['id']


# __________________ Способ оплаты __________________
# @admin.register(PayMethod)
# class PayMethodAdmin(admin.ModelAdmin):
#     list_display = ['pay_method', 'id']
#     readonly_fields = ['id']


# @admin.register(DeliveryMethod)
# class DeliveryMethodAdmin(admin.ModelAdmin):
#     list_display = ['delivery_method']
