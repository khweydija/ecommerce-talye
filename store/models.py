from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey


class Fournisseur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    nomboutique = models.CharField(max_length=200)
    def _str_(self):
        return self.nom

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='media/images/', default='media/images/default.png')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE) 
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']  

    def __str__(self):
        return self.title           

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom  
    
    
    




