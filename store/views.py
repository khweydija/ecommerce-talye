from ast import FormattedValue
from multiprocessing import context
from tkinter.tix import Form
from django import forms
from django.shortcuts import redirect, render

#lile user
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNewUser, ProdForm
from django.contrib import messages
from django.contrib.auth import authenticate  ,logout
from django.contrib.auth import login as mylogin

#lile models
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse


#lilte CRUD
from django.http import HttpResponse
from django.contrib import messages


#ya lembarkin ha4iiiiiiiiii CRUD lmesrugue

def affiche(request):
    prod = Product.objects.order_by('-id')
    return render(request, 'CRUD/indexx.html', {'prod':prod})


def delete_produit(request, id):
     prod = Product.objects.get(id=id)
     prod.delete()
     # After the operation was Deleted
     messages.success(request, 'Deleted successful!')
     return redirect("/indexx")


def modifier(requst, id):
    prod = Product.objects.get(id=id)
    return render(requst, 'CRUD/edit.html',{'prod':prod})


def update_produit(request, id):
     prod = Product.objects.get(id=id)
     if request.method == "POST" :
        form =  ProdForm(request.POST, request.FILES, instance = prod)
        if form.is_valid():
            form.save()
            # After the operation was Update
            messages.success(request, 'Update successful!')
            # redirect to some other page
            return redirect("/indexx")
        # After the operation was fail
        message = 'Something we are wrong!'
        return render(request, 'CRUD/edit.html',{'message':message,'prod':form})
     else:
         form = Product.objects.get(id=id)
         prod = ProdForm(instance = form)
         content = {'prod':prod,'id':id}
         return render(request, 'CRUD/edit.html',content)



def create_produit(request):
    form = ProdForm()
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = ProdForm(request.POST, request.FILES)
        # Validate the form

        if form.is_valid():
            try:
                form.save()
                # After the operation was successful
                messages.success(request, "Created successful!")
                # redirect to some other page
                return redirect('/indexx')
            except:
                message = "Something we are wrong!"
                form = ProdForm()
            return render(request, 'CRUD/create.html',{'message':message,'form':form})
    else:
        # Create an empty form instance
        form = ProdForm()
    return render(request, 'CRUD/create.html',{'form':form})

##################################################################################################################


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


#def Userlogin(request):  
       # if request.method == 'POST': 
         #   username = request.POST.get('username')
          #  password = request.POST.get('password')
           # user = authenticate(request , username=username, password=password)
           # if user is not None:
            # mylogin(request, user)
             #return redirect('home')
           # else:
             #   messages.info(request, 'Credentials error')
        #context = {}
       # return render(request , 'login.html', context )
    

def Frnlogin(request):  
  
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            try:
                frn = Fournisseur.objects.get(user=user)
                if user is not None:
                    print("is  mewjud")
                    mylogin(request, user)
                    return redirect('indexx')
                else:
                    messages.info(request, 'le fournisseur pas ici wallahi error')
            except:
                print("frn mahu 5alg")
                messages.info(request, 'le fournisseur pas ici wallahi error')
        context = {}
        return render(request , 'login.html', context ) 
    

def Userlogout(request):  
    logout(request)
    return redirect('home')
  
       
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
