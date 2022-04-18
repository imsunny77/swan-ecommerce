from django.contrib import admin
from order.models import *
# Register your models here.
admin.site.register(Cart)


class CartItemAdmin(admin.ModelAdmin):
    fields = ['cart_id','product','product_name','product_category','price', 'quantity','total_price']
    list_display = ['cart_id','product','product_name','product_category','price', 'quantity','total_price']

admin.site.register(CartItem,CartItemAdmin)
