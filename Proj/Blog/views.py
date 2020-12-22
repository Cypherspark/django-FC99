from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request) :
    return render(request, 'index.html')

def form(request):
    if request.method == "GET":
        print("{}".format(request.method))
        a = User.objects.all()
        mylist = {"data" : a}
        return render(request, "form.html", context = mylist)

    if request.method == "POST":    
        a = User.objects.create(username= request.POST["username"], password= request.POST["password"])  
        context = {"data": "ok"}
        # Product.objects.create(title = ..)
        return render(request, "form.html", context = context) 


def print_prime(a):
    pass

