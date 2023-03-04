from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, TextInput, EmailField

from store.models import Product


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
        
 

       


class ProdForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = ['title',' price',' description','category','image ',' date_added ']
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            "price": forms.NumberInput(attrs={'class':'form-control','min':'0','placeholder':'Enter Number'}),
            "description":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            # "category"  : forms.ChoiceField(),
            "image" : forms.FileInput(attrs={ 'class':'form-control'}),
        }
