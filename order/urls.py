# from administration.models import Branch
from django.urls import path
from order import api

app_name = 'order'
urlpatterns = [
    path('api/add-to-cart/<str:product_id>/',           api.AddToCart.as_view()),       #   add product to 

]
