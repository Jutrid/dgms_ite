from django.contrib import admin
from .models import News, Places

# Register your models here.

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description', 'img')

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'description', 'img')

admin.site.register(News, NewAdmin)
admin.site.register(Places, PlacesAdmin)

