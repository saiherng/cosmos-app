from atexit import register
from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('name', 'phone_number', 'address', 'email')
    fields = ['name', 'phone_number', 'address', 'email']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer',
                    'placed_at', 'payment', 'payment_account']
    list_filter = ['customer']


@ admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice','product', 'quantity', 'unit_price']
    list_filter = ['invoice']


@ admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
