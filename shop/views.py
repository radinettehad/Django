# shop/views.py  
from django.shortcuts import render  
from .models import Product, Category  
from django.db.models import Q  

def home(request):  
    products = Product.objects.all()  
    if not products:  
        message = "محصولی یافت نشد."  
    else:  
        message = ""  
    return render(request, 'shop/home.html', {'products': products, 'message': message})

def product_list(request):  
    products = Product.objects.all()  
    if 'q' in request.GET:  
        query = request.GET['q']  
        products = products.filter(Q(name__icontains=query))  
    return render(request, 'shop/product_list.html', {'products': products})  

def product_detail(request, product_id):  
    product = Product.objects.get(id=product_id)  
    return render(request, 'shop/product_detail.html', {'product': product})