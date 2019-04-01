from django.contrib import admin

# Register your models here.

from .models import Product, Manufacturer

admin.site.register(Product)
admin.site.register(Manufacturer)
