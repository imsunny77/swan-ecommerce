# from administration.models import Branch
from django.urls import path
from administration import views
app_name = 'administration'
urlpatterns = [
    path('',        views.HomePageView.as_view(), name='home'),
    path('sign-up/',views.add_user, name='add_user'),

]
