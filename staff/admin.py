from django.contrib import admin

from .models import *


@admin.register(Curier)
class CurierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'id']
