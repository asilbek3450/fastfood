from django.contrib import admin

from fastfood.models import ProductCategory, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
