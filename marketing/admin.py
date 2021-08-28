from django.contrib import admin

from .models import *


@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'discount']
