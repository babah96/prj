from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Stock.models import Service, StockEn, Sorti, STOCK,Utilisateurs,User
from django.db.models import Max

from django.contrib.auth import authenticate, login, logout
from Stock.forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('Acceil')
                
    context = {'form': forms, }
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Aceeil(request):
    
    
    l=User.objects.filter()
    

    products = STOCK.objects.all()
    total_Stocknkc = StockEn.objects.filter(STOCKT="nkc").count()
    total_Sortinkc = Sorti.objects.filter(STOCKT="nkc").count()
    total_Stockfm = StockEn.objects.filter(STOCKT="fm").count()
    total_Sortifm = Sorti.objects.filter(STOCKT="fm").count()
    ts1 = STOCK.objects.filter(STOCKT="nkc").count()
    ts2 = STOCK.objects.filter(STOCKT="fm").count()
    NPT = STOCK.objects.count()
    #nbg = STOCK.objects.filter.count()
    nservice=Service.objects.count()
    nbg=ts1+ts2

    context = {
        #'nbg':nbg,
        'NPT':NPT,
        'Stocknkc': total_Stocknkc,
        'Sortinkc': total_Sortinkc,
         'Stockfm': total_Stockfm,
        'Sortifm': total_Sortifm,
        'tsnkc':ts1,
        'tsfm':ts2,
        'nservice':nservice,
        'u':l,
        'nbg':nbg,
        "STOCK": products,
                  }
    return render(request,'Aceeil.html',context)
    
