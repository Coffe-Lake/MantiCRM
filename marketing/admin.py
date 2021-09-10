from django.contrib import admin

from .models import *


@admin.register(Discounts)
class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'discount']
