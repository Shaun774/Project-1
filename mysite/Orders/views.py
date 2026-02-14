from django.shortcuts import render,redirect
from .models import Order
from .forms import Orderform

# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = Orderform(request.POST)
        if form.is_valid():

            form.save()
            return redirect("ordersucess")
    else:
        form = Orderform()
        return render(request,"order.html",{'form':form})

def ordersucess(request):
    return render(request,"ordersucess.html")