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
    try:
        billing_address = user.address.get(is_billing=True)
        shipping_address = user.address.get(is_shipping=True)

    except:
        billing_address = user.address.last()
        shipping_address = user.address.last()

    total_payable = 0
    for i in cart_items:
        total_payable = total_payable + i.total_price
        total_payable = total_payable
    cart_obj.total_price=total_payable 
    cart_obj.save()
    mail_order_detail(user.email,cart_obj.id,user,billing_address.id,shipping_address.id,total_payable)
    # task_mail_order_detail.delay
    context = { 
        'cart_items':cart_items,
        'cart_obj':cart_obj,
        'user':user,
        'billing_address':billing_address,
        'shipping_address':shipping_address,
        'total':total_payable,
    }
    return render(request,'order/confirmation.html',context)
