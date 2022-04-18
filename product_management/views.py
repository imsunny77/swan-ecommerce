import re
from django.shortcuts import render
from product_management.models import *
from django.views.generic import * 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def product_detail(request, pk):
    product_obj = Product.objects.get(pk=pk)
    return render(request,'product_management/product_detail.html',{'object':product_obj})

class ProductList(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        qs = Product.objects.all().order_by('-quantity') #filter(display_status=0) 
        # filter_qs =ProductFilter(self.request.GET, qs)
        # context['filter'] =  filter_qs
        paginated_filtered_list = Paginator(qs,10)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginated_filtered_list.get_page(page_number)
        context['categories'] = ProductCategory.objects.all()
        return context 