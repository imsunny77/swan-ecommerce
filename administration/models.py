import uuid
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import AbstractUser
from swan_ecommerce.models import BaseModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class ShippingAddress(BaseModel):
    address_1   = models.CharField('Address Line 1', max_length=50, null=True)
    address_2   = models.CharField('Address Line 2', max_length=50, null=True, blank=True)
    city        = models.CharField('City', max_length=50, null=True)
    state       = models.CharField('State', max_length=50, null=True)
    zipcode     = models.CharField('Zipcode', max_length=50, null=True)
    country     = CountryField('Country', null=True, blank=True)
    is_billing  = models.BooleanField('Do you want to set as default billing address?', default=False)
    is_shipping = models.BooleanField('Do you want to set as default shipping address?', default=False)

    def billing(self):
        if self.is_billing:
            return "default Billing Address"
        else:
            return '-'

    def shipping(self):
        if self.is_shipping:
            return "default Shipping Address"
        else:
            return '-'

class RootUser(AbstractUser):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email       = models.EmailField('Email', null=True)
    phone_no    = PhoneNumberField('Phone Number', null=True)
    phone_no_2  = PhoneNumberField('Alternet Phone Number', null=True, blank=True)
    address     = models.ManyToManyField(ShippingAddress)

    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email
        super(RootUser, self).save(*args, **kwargs)

