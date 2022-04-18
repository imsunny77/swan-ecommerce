from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from administration.forms import *
from django.contrib.auth.decorators import login_required
from product_management.models import *
from order.models import *

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

def my_profile(request):
    user = RootUser.objects.get(username=request.user.username)
    return render(request,'administration/my_profile.html',{'object':user})


def edit_user(request,pk):
    user = RootUser.objects.get(pk=pk)
    form = RootUserForm(request.POST or None, instance = user)
    if form.is_valid():
        form.save()
        return redirect('administration:my_profile')
    return render(request,'administration/edit_profile.html',{'form':form})

