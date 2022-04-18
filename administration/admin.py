from django.contrib import admin
from .models import *

admin.site.register(ShippingAddress)

class RootUserAdmin(admin.ModelAdmin):
    fields = ['email','first_name', 'last_name', 'phone_no','phone_no_2','address']

admin.site.register(RootUser,RootUserAdmin)
