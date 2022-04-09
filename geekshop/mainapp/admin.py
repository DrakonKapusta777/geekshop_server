from django.contrib import admin

from mainapp.models import Product, ProductCategories

admin.site.register(ProductCategories)
admin.site.register(Product)
