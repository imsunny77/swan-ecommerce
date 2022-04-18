from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from product_management.models import *
from order.models import *

class AddToCart(APIView):
    def post(self, request, format=None, **kwargs):
        if 'current_cart' in request.session.keys():
            current_cart = request.session['current_cart']
            cart_obj = Cart.objects.get(cart_id = current_cart)
        else:
            cart_obj = Cart.objects.create()
            request.session['current_cart'] = cart_obj.cart_id
            # cart_obj.save()
        current_cart = request.session['current_cart']
        quantity = request.POST['quantity']
        print(current_cart,quantity,product_id)

        product_id = get_object_or_404(Product,id = kwargs['product_id'])
        item_obj, created= CartItem.objects.update_or_create(product=product_id)
        item_obj.cart_id = cart_obj
        item_obj.product_name = product_id.product_name
        item_obj.product_category = product_id.product_category.category
        item_obj.price = product_id.price
        item_obj.quantity = quantity
        item_obj.save()

        return JsonResponse({"updated_cart": 'updated_cart'})
