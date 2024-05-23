from django.db import models
from cataleg.models import Producte
from client.models import Client
from django.utils import timezone

# Create your models here.


class Carreto(models.Model):
    producte = models.ManyToManyField(Producte)
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    actiu = models.BooleanField(default=False)
    preuTotal = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)