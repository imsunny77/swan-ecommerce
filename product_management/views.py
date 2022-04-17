import re
from django.shortcuts import render
from product_management.models import *
# Create your views here.
def product_detail(request, pk):
    product_obj = Product.objects.get(pk=pk)
    return render(request,'product_management/product_detail.html',{'object':product_obj})