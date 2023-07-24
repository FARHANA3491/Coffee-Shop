from django.shortcuts import render,redirect
from .models import products
from .forms import BookingForm

# Create your views here.


def menu(request):
    dict_product = {
        'products' : products.objects.all()
    }
    return render(request,'menu.html',dict_product)

def index(request):
    dict_prod = {
        'product' : products.objects.all()
    }
    return render(request,'index.html',dict_prod)


    
def booknow(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error detected",form.errors)
            return redirect('/')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booknow.html',dict_form)

