from django.contrib import admin
from .models import Product, Order


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Id', 'name', 'price', 'quantity')
    search_fields = ('name',)
    list_filter = ('price',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('Id', 'product', 'quantity', 'order_date')
    search_fields = ('product__name',)
    list_filter = ('order_date',)