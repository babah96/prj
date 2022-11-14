from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from Stock import models 
from django.views.generic import ListView
from .models import (
    STOCK, Fournisseur, Service, Sorti ,StockEn,User,Utilisateurs
)
from .forms import (
    
    SortieEnregistrer,StockEnregistrer,SEnregistrer,FEnregistrer,EntrerEnregistrer,UtilisateurForm
    
)
# Create your views here.




@login_required(login_url='login')
def AjouterUtilisateur(request):
    forms = UtilisateurForm()
    if request.method == 'POST':
        forms = UtilisateurForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            STOCKT = forms.cleaned_data['STOCKT']
            email = forms.cleaned_data['email']
           
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                if STOCKT == 'nkc':
                    user = User.objects.create_user(
                        username=name, password=password,
                        email=email, Utilisateur=True,STOCKTNKT=True 
                        )
                        
               
                       
                                      
                Utilisateurs.objects.create(user=user, name=name, address=address,STOCKT=STOCKT)
                return redirect('Utilisateur')
    l=User.objects.filter()
    context = {
        'form': forms,'u':l
    }
    return render(request, 'Pages/Ajouteuser.html', context)


class UtilisateursListView(ListView):
    model = Utilisateurs
    template_name = 'Pages/Utilisateur.html'
    context_object_name = 'Utilisateurs'

@login_required(login_url='login')
def deluser(request,id):
    deluser=Utilisateurs.objects.get(id=id)
    deluser.delete()
    return redirect('Utilisateur')



@login_required(login_url='login')
def StocknktEntrer(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = EntrerEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = EntrerEnregistrer(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           Article=STOCK.objects.get(id=id)
           QTEx=STOCK.objects.get(id=id).QTEx
           QTEn=forms.cleaned_data['QTEn']
           STOCKT=STOCK.objects.get(id=id).STOCKT       
           
           Fournisseur=forms.cleaned_data['Fournisseur']
           
           msg='Stock Entrer Enregistrer'
           StockEn.objects.create(
                Designation=Designation,
                Article=Article,
                QTEx=QTEx,
                QTEn=QTEn,
                STOCKT=STOCKT,
                Fournisseur=Fournisseur,

            )

        d=STOCK.objects.get(id=id).Designation
        k=STOCK.objects.get(id=id).Article
        q1=STOCK.objects.get(id=id).QTEx+forms.cleaned_data['QTEn'] 
        q2= STOCK.objects.get(id=id).QTEn+forms.cleaned_data['QTEn']
        q3= STOCK.objects.get(id=id).QTS
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1,QTEn=q2,QTS=q3)
        
    l=User.objects.filter() 
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg,'u':l
    }
 
    return render(request,'Pages/StocknktEntrer.html',context)
@login_required(login_url='login')
def Stocks(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    s=Utilisateurs.objects.get(id=id3).STOCKT
    produit=models.StockEn.objects.filter(STOCKT=s)
    l=User.objects.filter()
    context={
        'Stock':produit,'u':l
    }
    return render(request,'Pages/Stock.html',context)

def Stocks2(request):
    
    produit=models.StockEn.objects.filter(STOCKT="nkc")
    l=User.objects.filter()
    context={
        'Stock':produit,'u':l
    }
    return render(request,'Pages/Stock.html',context)


@login_required(login_url='login')
def delStock(request,id):
    delStock=StockEn.objects.get(id=id)
    delStock.delete()
    return redirect('Stocks')


@login_required(login_url='login')
def StocknktSortie(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = SortieEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = SortieEnregistrer(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           Article=STOCK.objects.get(id=id)
           QTS=forms.cleaned_data['QTS']         
           QTR=STOCK.objects.get(id=id).QTEx-QTS
           STOCKT=STOCK.objects.get(id=id).STOCKT  
           Service=forms.cleaned_data['Service']
           
           msg='Stock Sortie Enreistrer '
           Sorti.objects.create(
                Designation=Designation,
                STOCKT=STOCKT,
                QTS=QTS,
                QTR=QTR,
                Service=Service,

            )
        d=STOCK.objects.get(id=id).Designation
        k=STOCK.objects.get(id=id).Article
        q1=STOCK.objects.get(id=id).QTEx-forms.cleaned_data['QTS'] 
        q2=STOCK.objects.get(id=id).QTS+forms.cleaned_data['QTS'] 
        q3=STOCK.objects.get(id=id).QTEn
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1,QTS=q2,QTEn=q3)
    l=User.objects.filter()
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg,'u':l
    }
    return render(request,'Pages/StocknktSortie.html',context)

@login_required(login_url='login')
def Sortis(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    s=Utilisateurs.objects.get(id=id3).STOCKT
    sorti=models.Sorti.objects.filter(STOCKT=s)
    l=User.objects.filter()
    context={
        'sorti':sorti,'u':l
    }
    return render(request,'Pages/sortis.html',context)

@login_required(login_url='login')
def Sortis2(request):
    sorti=models.Sorti.objects.filter(STOCKT="nkc")
    l=User.objects.filter()
    context={
        'sorti':sorti,'u':l
    }
    return render(request,'Pages/sortis.html',context)


@login_required(login_url='login')
def delSortie(request,id):
    delSortie=Sorti.objects.get(id=id)
    delSortie.delete()
    return redirect('sorti')



@login_required(login_url='login')
def AjouteService(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    forms = SEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = SEnregistrer(request.POST)
        if forms.is_valid():
            Nom = forms.cleaned_data['Nom']

            STOCKT=Utilisateurs.objects.get(id=id3).STOCKT
            msg=' Service Enregister'
            Service.objects.create(
                Nom=Nom,STOCKT=STOCKT
            )
    l=User.objects.filter()
    context = {
        'form': forms,
        'msg':msg,'u':l
    }
    return render(request,'Pages/AjouteService.html',context)

@login_required(login_url='login')
def Services(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    s=Utilisateurs.objects.get(id=id3).STOCKT
    Service=models.Service.objects.filter(STOCKT=s)
    l=User.objects.filter()
    context={
        'Service':Service,'u':l
    }
    return render(request,'Pages/Service.html',context)
@login_required(login_url='login')
def Services2(request):
    
    Service=models.Service.objects.filter(STOCKT="nkc")
    l=User.objects.filter()
    context={
        'Service':Service,'u':l
    }
    return render(request,'Pages/Service.html',context)



@login_required(login_url='login')
def delService(request,id):
    delService=Service.objects.get(id=id)
    delService.delete()
    return redirect('Service')


@login_required(login_url='login')
def AjoutFournisseur(request):
    forms = FEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = FEnregistrer(request.POST)
        if forms.is_valid():     
            Nom = forms.cleaned_data['Nom']
            Abrevation = forms.cleaned_data['Abrevation']
            NomDirecteur = forms.cleaned_data['NomDirecteur']
           
            Tel = forms.cleaned_data['Tel']
            Email = forms.cleaned_data['Email']
            Domaine = forms.cleaned_data['Domaine']
           
            msg='Founiseur Ajouter'          
            Fournisseur.objects.create(             
                Nom=Nom,
                Abrevation=Abrevation,
                NomDirecteur=NomDirecteur,
               
                Tel=Tel,
                Email=Email,
                Domaine=Domaine,
                          
            )
    l=User.objects.filter()
    context = {
        'form': forms,
        'msg':msg,'u':l
    }
    return render(request,'Pages/AjoutFournisseur.html',context)


@login_required(login_url='login')
def Fournisseurs(request):
    Fournisseur=models.Fournisseur.objects.filter()
    context={
        'Fournisseur':Fournisseur
    }
    return render(request,'Pages/Fournisseur.html',context)

@login_required(login_url='login')
def delFournisseur(request,id):
    delFournisseur=Fournisseur.objects.get(id=id)
    delFournisseur.delete()
    return redirect('Fournisseur')


@login_required(login_url='login')
def STOCKS(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    s=Utilisateurs.objects.get(id=id3).STOCKT
    STOCK1=models.STOCK.objects.filter(STOCKT=s)
    l=User.objects.filter()
    
    context={
        'STOCK1':STOCK1,'u':l
    }
    return render(request,'Pages/STOCKS.html',context)

@login_required(login_url='login')
def STOCKS2(request):
    
    
    STOCK1=models.STOCK.objects.filter(STOCKT="nkc")
    l=User.objects.filter()
    context={
        'STOCK1':STOCK1,'u':l
    }
    return render(request,'Pages/STOCKS.html',context)


@login_required(login_url='login')
def AjoutDesignation(request,id):
    id2=User.objects.get(id=id).id
    id3=id2-1
    forms = StockEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = StockEnregistrer(request.POST)
        if forms.is_valid():     
            Designation= forms.cleaned_data['Designation']
            STOCKT=Utilisateurs.objects.get(id=id3).STOCKT 
           
            msg='Designation Enregister'          
            STOCK.objects.create(             
                Designation=Designation,STOCKT=STOCKT
               
            )
    l=User.objects.filter()
            
    context = {
        'form': forms,
        'msg':msg,'u':l
    }
    return render(request,'Pages/AjoutDesignation.html',context)




