# shop/urls.py
from django.urls import path
from .views import home, product_list, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('search/', product_list, name='search'),
]