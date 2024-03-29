from django.contrib import admin
from .models import Product, Category 
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'flavour',
    )
    

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
