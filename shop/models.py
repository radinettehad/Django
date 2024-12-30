# shop/models.py  
from django.db import models  

class Category(models.Model):  
    name = models.CharField(max_length=255)  

    def __str__(self):  
        return self.name  

class Product(models.Model):  
    name = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.name  

class Customer(models.Model):  
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    phone_number = models.CharField(max_length=15)  

    def __str__(self):  
        return self.name