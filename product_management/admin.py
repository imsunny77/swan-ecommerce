from django.contrib import admin
from product_management.models import *

# class ProductCategoryAdmin(admin.ModelAdmin):
#     fields = ['updated','category', ]
#     list_display = ['category',]
#     list_editable = ['category',]

admin.site.register(ProductCategory)

class ProductAdmin(admin.ModelAdmin):
    fields = ['thumbnail_image','product_name','product_category','description', 'price', 'quantity', 'in_stock','sold']
    list_display = ['updated', 'product_name','product_category','price', 'quantity', 'in_stock', 'sold',]
    list_editable = ['product_category','price','quantity',]
    readonly_fields = ('in_stock','sold')

admin.site.register(Product, ProductAdmin)
