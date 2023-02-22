from ast import FormattedValue
from multiprocessing import context
from tkinter.tix import Form
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm



from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate  ,logout
from django.contrib.auth import login as mylogin

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
  
       

    
# Create your views here.
