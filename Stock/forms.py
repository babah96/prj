from django import forms
from django.forms.widgets import Widget

from .models import Service, StockEn,Sorti,Fournisseur,STOCK



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))



class UtilisateurForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
        
        
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
  
   
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class AdminForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))









class FEnregistrer(forms.ModelForm):
     class Meta:
        model = Fournisseur
        fields = [
            'Nom','Abrevation','NomDirecteur','Tel','Email','Domaine'
        ]

        widgets = {
            'Nom': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Nom'
            }),
            'Abrevation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Abrevation'
            }),
            'NomDirecteur': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'NomDirecteur'
            }), 
           
            'Tel': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Tel'
            }), 
            'Email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Email'
            }), 
            'Domaine': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Domaine'
            }), 
           
            
        }

class SEnregistrer(forms.ModelForm):
     class Meta:
        model = Service
        fields = [
            'Nom'
        ]

        widgets = {
            'Nom': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Nom'
            }),     
            
        }




class EntrerEnregistrer(forms.ModelForm):
    class Meta:
        model = StockEn
        fields = [
            'QTEn', 'Fournisseur'
        ]

        widgets = {
            
            
            'QTEn': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEn'
            }),
           
           
            'Fournisseur': forms.Select(attrs={
                'class': 'form-control', 'id': 'Fournisseur'
            }),
            
            
        }

class SortieEnregistrer(forms.ModelForm):
    class Meta:
        model = Sorti
        fields = [
             'Service',  'QTS'
        ]

        widgets = {
            
            'Service': forms.Select(attrs={
                'class': 'form-control', 'id': 'Service'
            }),
    
            'QTS': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTS'
            }),
           
            
            
        }


class StockEnregistrer(forms.ModelForm):
    class Meta:
        model = STOCK
        fields = [
            'Designation'
        ]

        widgets = {
            'Designation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Designation'
            }),
         
           
        }


