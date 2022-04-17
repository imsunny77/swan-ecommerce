from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from administration.forms import *
from django.contrib.auth.decorators import login_required
from product_management.models import *

class HomePageView(TemplateView):
    template_name = "administration/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()[:20]
        context['uppcoming_product_list'] = Product.objects.filter(quantity=0)[:20]
        context['latest_product'] = Product.objects.all().last()
        return context

def add_user(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'registration/sign_up.html',{'form':form})