from django.db import models
from people.models import *

# Create your models here.

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    wrestlers = models.ManyToManyField(Wrestler, related_name='promotions', blank=True,)

    def __str__(self):
        return self.name