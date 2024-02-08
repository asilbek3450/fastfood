from django.contrib import admin

from fastfood.models import ProductCategory, Product, BookTable

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(BookTable)
