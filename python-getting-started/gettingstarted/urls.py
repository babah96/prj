from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/



from django.contrib import admin
from django.urls import path
from Stock import views
from Stock.views import  ( Services2, Services3, Stocks, Sortis, StocknktEntrer,StocknktSortie,
                          AjoutFournisseur,AjouteService,Fournisseurs,Services,STOCKS2,STOCKS3,Stocks2,Stocks3,Sortis2,Sortis3,deluser,
                             delSortie,delService,delStock,delFournisseur,STOCKS,AjoutDesignation ,
                             AjouterUtilisateur,UtilisateursListView,
                             
                             )
from .views import Aceeil
from .views import login_page, logout_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Stocks/<id>/',Stocks,name='Stocks'),
     path('Stocks2/',Stocks2,name='Stocks2'),
      path('Stocks3/',Stocks3,name='Stocks3'),
    path('',Aceeil,name='Acceil'),
    path('delSortie/<id>/',delSortie,name='delSortie'),
    path('delFournisseur/<id>/',delFournisseur,name='delFournisseur'),
    path('delService/<id>/',delService,name='delService'),
    path('delStock/<id>/',delStock,name='delStock'),
    path('sorti/<id>/',Sortis,name='sorti'),
    path('sorti2/',Sortis2,name='sorti2'),
    path('sorti3/',Sortis3,name='sorti3'),
    path('StocknktEntrer/<id>/',StocknktEntrer,name='StocknktEntrer'),
    path('StocknktSortie/<id>/',StocknktSortie,name='StocknktSortie'),
    path('AjoutFournisseur/',AjoutFournisseur,name='AjoutFournisseur'),
    path('AjouteService/<id>/',AjouteService,name='AjouteService'),
    path('deluser/<id>/',deluser,name='deluser'),
    path('Service/<id>/',Services,name='Service'),
    path('Service3/',Services3,name='Service3'),
    path('Service2/',Services2,name='Service2'),
    path('Fournisseur/',Fournisseurs,name='Fournisseur'),
    path('STOCKS/<id>/',STOCKS,name='STOCKS'),
    path('STOCKS2/',STOCKS2,name='STOCKS2'),
    path('STOCKS3/',STOCKS3,name='STOCKS3'),
    path('AjoutDesignation/<id>/',AjoutDesignation,name='AjoutDesignation'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('Utilisateur/', UtilisateursListView.as_view(), name='Utilisateur'),
    path('Ajouteuser/', AjouterUtilisateur, name='Ajouteuser'),
    
    path('<str:room>/', views.room, name='room'),
    path('checkview/<id>/<id2>/', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
   
    

]
