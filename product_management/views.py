import re
from urllib import request
from django.shortcuts import render
from product_management.models import *
from django.views.generic import * 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def product_detail(request, pk):
    product_obj = Product.objects.get(pk=pk)
    return render(request,'product_management/product_detail.html',{'object':product_obj})

class ProductList(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        category = ''
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            category = ProductCategory.objects.get(id=category)
            qs = Product.objects.filter(product_category=category).order_by('-quantity') 
        else:
            qs = Product.objects.all().order_by('-quantity') #filter(display_status=0) 
        # filter_qs =ProductFilter(self.request.GET, qs)
        # context['filter'] =  filter_qs
        paginated_filtered_list = Paginator(qs,10)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginated_filtered_list.get_page(page_number)
        context['categories'] = ProductCategory.objects.all()
        context['current_category'] = category
        context['all_product'] = Product.objects.all().count()
        return context 

def filter_product(request):
    context={}
    query =request.GET.get('q')
    print(query)
    qs = Product.objects.filter(Q(product_name__icontains=query) | 
            Q(product_category__category__icontains=query))
    paginated_filtered_list = Paginator(qs,10)
    page_number = request.GET.get('page')
    context['page_obj'] = paginated_filtered_list.get_page(page_number)
    context['categories'] = ProductCategory.objects.all()
    context['current_category'] = query
    context['all_product'] = Product.objects.all().count()
    return render(request,'product_management/product_list.html',context)