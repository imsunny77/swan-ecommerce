import re
from django.shortcuts import render
from order.models import *
from .utils import mail_order_detail
def cart_list(request):
    if 'current_cart' in request.session.keys():
        current_cart = request.session['current_cart']
        cart_obj = Cart.objects.get(cart_id = current_cart)
    else:
        cart_obj = Cart.objects.create()
        request.session['current_cart'] = cart_obj.cart_id
        current_cart = request.session['current_cart']

    cart_items = CartItem.objects.filter(cart_id = cart_obj)
    total_payable = 0
    for i in cart_items:
        total_payable = total_payable + i.total_price
        total_payable = total_payable
    context = { 
        'cart_items':cart_items,
        'total_payable':total_payable,
        'cart_obj':cart_obj
    }
    return render(request,'order/cart_list.html',context)

def confirmation(request,pk):
    cart_obj = Cart.objects.get(pk=pk)
    cart_items = CartItem.objects.filter(cart_id = cart_obj)
    user = RootUser.objects.get(username = request.user.username)
    address = user.address.last()
    total_payable = 0
    for i in cart_items:
        total_payable = total_payable + i.total_price
        total_payable = total_payable
    cart_obj.total_price =total_payable 
    cart_obj.save()
    mail_order_detail(user.email)
    context = { 
        'cart_items':cart_items,
        'cart_obj':cart_obj,
        'user':user,
        'address':address,
        'total':total_payable
    }
    return render(request,'order/confirmation.html',context)
