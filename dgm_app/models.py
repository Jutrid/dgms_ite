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

class Immigres(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    postnom = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1)
    date_nais = models.DateField()
    nationalite = models.CharField(max_length=50)
    pays_residence = models.CharField(max_length=50)
    adress_residence = models.CharField(max_length=100)
    profession = models.CharField(max_length=30)
    provenance = models.CharField(max_length=30)
    img = models.ImageField(upload_to='photo_immigré')

    class Meta():
        db_table = 'Immigrés'

    def __str__(self):
        return self.nom

class Documents(models.Model):
    num_visa = models.CharField(max_length=30)
    num_carte_id = models.CharField(max_length=30)

    class Meta():
        db_table = 'Documents'

    def __str__(self):
        return self.num_visa

class Sejours(models.Model):
    but = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    ville = models.CharField(max_length=20)

    class Meta():
        db_table = 'Sejours'

    def __str__(self):
        return self.but

class Demandes(models.Model):
    sejour = models.ForeignKey(Sejours, on_delete=models.CASCADE)
    immigre = models.ForeignKey(Immigres, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    avis = models.CharField(max_length=1, default='N')
    date_demande = models.DateTimeField(auto_now=True)
    lu = models.BooleanField(default=False)

    class Meta():
        db_table = 'Demandes'
