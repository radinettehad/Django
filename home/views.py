from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello World</h1>")
# Create your views here.
def index(request):
    return render(request,'index.html')