from django.db import models
from django.utils import timezone

# Create your models here.


class Client(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100) 
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return self.nom