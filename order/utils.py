
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
import os
from django.template.loader import get_template


def mail_order_detail(email):    #(obj.customer_email, obj.receipt.path)
    message='Please find your order details you have just placed.'
    subject='Your Order Details'
    html_content = 'Please find your order details you have just placed.'
    email=EmailMultiAlternatives(subject,message,settings.EMAIL_HOST_USER, [email, ])
    email.attach_alternative(html_content, "text/html")
    try:
        email.send()
    except:
        pass
