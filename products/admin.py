from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'slug', 'available', 'id']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ['name', 'price', 'category', 'composition', 'slug', 'available', 'number_of_stock', 'id']
    search_fields = ('name', 'price', 'slug')
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at', 'id']
