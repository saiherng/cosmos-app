from django.contrib import admin

# Register your models here.
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('name', 'phone_number', 'address', 'email')
    fields = ['name', 'phone_number', 'address', 'email']


admin.site.register(Customer, CustomerAdmin)


admin.site.register(Invoice)
