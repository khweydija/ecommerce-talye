# from operator import index
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('detail', views.detail, name="detail"),
    path('checkout', views.checkout, name="checkout"),
    path('confirmation', views.confimation, name="confirmation" ),
    
    path('register/' ,views.registre, name="register"),
    path('login/' ,views.Frnlogin, name="login"),
    path('logout/' ,views.Userlogout, name="logout"),
    path('indexx/',views.affiche,name="indexx"),
    path('update_stud/<int:id>', views.modifier),
    
   
    
]

    
