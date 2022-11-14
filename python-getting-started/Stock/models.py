from select import select
from typing import Type
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Admin = models.BooleanField(default=False)
    Utilisateur = models.BooleanField(default=False)
    STOCKTNKT = models.BooleanField(default=False)
    STOCKTfl= models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Utilisateurs(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    STOCKT=models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    Nom=models.CharField(max_length=100)
    Abrevation=models.CharField(max_length=100)
    NomDirecteur=models.CharField(max_length=100)
    Nif=models.IntegerField()
    Tel=models.IntegerField()
    Email=models.CharField(max_length=30)
    Domaine=models.CharField(max_length=100)
    RC=models.IntegerField()

    def __str__(self):
        return self.Nom

class Service(models.Model):
    Nom=models.CharField(max_length=30)
    STOCKT=models.CharField(max_length=220)
    def __str__(self):
        return self.Nom



class STOCK(models.Model):
    liblle=models.CharField(max_length=100)
    QTEx=models.IntegerField(default=0)
    QTEn=models.IntegerField(default=0)
    QTS=models.IntegerField(default=0)
    STOCKT=models.CharField(max_length=220)
    def __str__(self):
        return self.liblle
    
class StockEn(models.Model):
    liblle=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    QTEx=models.IntegerField()
    QTEn=models.IntegerField()
    Fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    STOCKT=models.CharField(max_length=220)
   
    date=models.DateField(auto_now_add=True)
   

class Sorti(models.Model):
    liblle=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    QTS=models.IntegerField()
    QTR=models.IntegerField()
    STOCKT=models.CharField(max_length=220)
 
    date=models.DateField(auto_now_add=True)

    
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)