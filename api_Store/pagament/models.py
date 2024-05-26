from django.db import models
from django.utils import timezone
from comandes.models import Comanda
from client.models import Client
# Create your models here.


class Pagament(models.Model):
    comanda = models.OneToOneField(Comanda, on_delete= models.CASCADE)
    numTarjeta = models.CharField(max_length=30)
    dataCad = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    actiu = models.BooleanField(default=False)
