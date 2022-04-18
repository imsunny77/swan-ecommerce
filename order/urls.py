# from administration.models import Branch
from django.urls import path
from order import api
from order import views

app_name = 'order'
urlpatterns = [
    path('api/add-to-cart/<str:product_id>/',           api.AddToCart.as_view()),       #   add product to 
    path('your-cart/',              views.cart_list,    name='cart_list'),
    path('confirmation/<str:pk>',   views.confirmation,    name='confirmation'),

    
]
