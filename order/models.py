from django.db import models
from swan_ecommerce.models import BaseModel
from administration.models import *
from product_management.models import *

from .choices import *
import string    
import random 
S = 5  # number of characters in the string.  

class Cart(BaseModel):
    cart_id     = models.CharField(('Order ID'),max_length=100, null=True)
    sub_total   = models.DecimalField(('Total'),max_digits=10, decimal_places=2, null=True)
    tax         = models.DecimalField(('Discount'),max_digits=10, decimal_places=2, default=18.00,null=True)
    total_price = models.DecimalField(('Total Payable'),max_digits=10, decimal_places=2, null=True)
    payment_status = models.IntegerField("Status", choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    def __str__(self):
        return (self.cart_id)

    def get_tax(self):
        tax_amt = (self.total_price * self.tax)/100
        return tax_amt

    def total_payable(self):
        tax_amt = (self.total_price * self.tax)/100
        total_payable = self.total_price + tax_amt
        return total_payable
        
    def save(self, *args, **kwargs):
        if not self.cart_id:
            cart_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            self.cart_id = cart_id
        super(Cart, self).save(*args, **kwargs)

class CartItem(BaseModel):
    cart_id         = models.ForeignKey(Cart,   on_delete= models.CASCADE,  null=True)
    product         = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
    product_name    = models.CharField(max_length=100, null=True)
    product_category= models.CharField(max_length=100, null=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity        = models.DecimalField("Purchased Quantity",max_digits=10, decimal_places=2, null=True)
    total_price     = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # def save(self, *args, **kwargs):
    #     if not self.total_price == 1:
    #         self.total_price = float(self.price) * float(self.quantity)
    #     super(CartItem, self).save(*args, **kwargs)