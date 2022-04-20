
from django.core.mail import send_mail, EmailMultiAlternatives,EmailMessage
from django.conf import settings
import os
from django.template.loader import get_template
from order.models import *

def mail_order_detail(email,cart_id,user,billing_address,shipping_address,total_payable):
    cart_obj = Cart.objects.get(id=cart_id)
    cart_items = CartItem.objects.filter(cart_id = cart_obj)
    user = RootUser.objects.get(username = user.username)
    billing_address = ShippingAddress.objects.get(id=billing_address)
    shipping_address = ShippingAddress.objects.get(id=shipping_address)
    message='Please find your order details you have just placed.'
    subject='Your Order Details'
    context = { 
        'cart_items':cart_items,
        'cart_obj':cart_obj,
        'user':user,
        'billing_address':billing_address,
        'shipping_address':shipping_address,
        'total':total_payable,
    }
    message = get_template("order/mail_order_detail.html").render(context)
    email=EmailMessage(
        subject=subject, 
        body=message, 
        from_email=settings.EMAIL_HOST_USER, 
        to=[email,],
    )
    email.content_subtype = "html"
    try:
        email.send()
    except:
        pass

