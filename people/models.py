from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.

class Wrestler(models.Model):
    name = models.CharField(max_length=255)
    height = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(220)])
    age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(150)])
    m = "Male"
    f = "Female"
    o = "Other"
    GENDERCHOICES = (
        (m, "Male"),
        (f, "Female"),
        (o, "Other"),
    )
    gender = models.CharField(max_length=10, 
        choices=GENDERCHOICES, default="Male")

    def __str__(self):
        return self.name