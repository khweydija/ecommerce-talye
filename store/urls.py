from django.urls import path
from . import views
from django.db import models


urlpatterns = [
    path('register/' ,views.registre, name="register"),
    path('login/' ,views.Userlogin, name="login"),
    path('logout/' ,views.Userlogout, name="logout"),
   
]

    
