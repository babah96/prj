from django.contrib import admin

from Stock.models import User, StockEn, Sorti,Service,Fournisseur,STOCK,Admins,Utilisateurs

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'Admin', 'Utilisateur']


admin.site.register(User, UserAdmin)
admin.site.register(StockEn)
admin.site.register(Sorti)
admin.site.register(Service)
admin.site.register(Fournisseur)
admin.site.register(STOCK)



class UtilisateursAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class AdminsAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Utilisateurs, UtilisateursAdmin)
admin.site.register(Admins, AdminsAdmin)



