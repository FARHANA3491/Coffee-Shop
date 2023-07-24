from django.shortcuts import render
from products.models import products

# Create your views here.

def index(request):
    dict_prod = {
        'product' : products.objects.all()
    }
    return render(request,'index.html',dict_prod)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def reservation(request):
    return render(request,'reservation.html')

def menu(request):
    return render(request,'menu.html')

def service(request):
    return render(request,'service.html')



