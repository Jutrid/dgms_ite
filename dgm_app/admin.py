from django.contrib import admin
from .models import News, Places, Documents, Demandes, Immigres, Sejours

# Register your models here.

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description', 'img')

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'description', 'img')

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_visa', 'num_carte_id')

class ImmigresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'postnom', 'sexe', 'img', 'nationalite')

class SejoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'but', 'date_debut', 'date_fin', 'ville')

class DemandesAdmin(admin.ModelAdmin):
    list_display = ('id', 'immigre', 'sejour', 'document', 'date_demande')

admin.site.register(News, NewAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Sejours, SejoursAdmin)
admin.site.register(Immigres, ImmigresAdmin)
admin.site.register(Demandes, DemandesAdmin)

