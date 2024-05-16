from django.db import models
from django.utils import timezone

# Create your models here.


class Producte(models.Model):
    nom = models.CharField(max_length=100)
    quantitat = models.IntegerField()
    preu = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=100)
    descripcio = models.TextField()
    dataCad = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    actiu = models.BooleanField(default=False)
    
    def _str_(self):
        return self.nom

class Cataleg(models.Model):
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    actiu = models.BooleanField(default=False)
    preuTotal = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

