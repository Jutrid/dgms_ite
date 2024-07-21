from django.db import models

# Create your models here.

class Places(models.Model):
    nom = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='places')

    def __str__(self):
        return self.nom
    
    class Meta():
        db_table = 'Places'
    
class News(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='news')

    class Meta(): 
        db_table = 'News'

    def __str__(self):
        return self.titre
    