from django.db import models
from django.utils import timezone
from carreto.models import Carreto
from client.models import Client
# Create your models here.


class Comanda(models.Model):
    carreto = models.OneToOneField(Carreto, on_delete= models.CASCADE)
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    actiu = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)