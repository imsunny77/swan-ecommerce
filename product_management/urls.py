# from administration.models import Branch
from django.urls import path
from product_management import views
app_name = 'product_management'

urlpatterns = [
    path('product-detail/<str:pk>', views.product_detail, name='product_detail'),
    path('all-products/',views.ProductList.as_view(), name='product_list'),

]
