from django.urls import path

from home import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
]