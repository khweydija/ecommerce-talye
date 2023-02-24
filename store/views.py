from ast import FormattedValue
from multiprocessing import context
from tkinter.tix import Form
from django import forms
from django.shortcuts import redirect, render

#lile user
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate  ,logout
from django.contrib.auth import login as mylogin

#lile models
from .models import Category, Product, Commande
from django.core.paginator import Paginator
from django.http import HttpResponse



def login(request):
    context = {}
    return render(request, 'login.html',context)


def registre(request):
    form = CreateNewUser()
    if request.method =='POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('usrname')
            messages.success(request,user + 'Created Successfully !')
            return redirect('login')
        
    context ={'form':form}    
    return render(request,'registre.html',context)


def Userlogin(request):  
  
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username=username, password=password)
            if user is not None:
             mylogin(request, user)
             return redirect('home')
            else:
                messages.info(request, 'Credentials error')
    
        context = {}

        return render(request , 'login.html', context )
    
    
    

def Userlogout(request):  
    logout(request)
    return redirect('login')
  
       
# l7oubi nedaniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')


    return render(request, 'shop/checkout.html') 

def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom}) 

#CRUD
         





    
# Create your views here.
