from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Move(models.Model):
    name = models.CharField(max_length=255)
    power = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    cost = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)], default=1)
    f = "High Flying"
    t = "Technical"
    b = "Brawling"
    s = "Submission"
    st = "Striking"
    g = "Grappling"
    m = "MMA"
    TYPECHOICES = (
        (f, "High Flying"),
        (t, "Technical"),
        (b, "Brawling"),
        (s, "Submission"),
        (st, "Striking"),
        (g, "Grappling"),
        (m, "MMA"),
    )
    move_type = models.CharField(max_length=12, 
        choices=TYPECHOICES, default="Male")

    def __str__(self):
        return self.name

class Wrestler(models.Model):
    name = models.CharField(max_length=255)
    height = models.PositiveIntegerField(validators=[MinValueValidator(60), MaxValueValidator(220)], default=60)
    age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(150)], default=10)
    strengh = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    speed = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    dex = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    heart = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    striking = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    grappling = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    moves = models.ManyToManyField(Move, related_name='known_moves', blank=True,)
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


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    wrestlers = models.ManyToManyField(Wrestler, related_name='promotions', blank=True,)
    s = "Scotland"
    n = "North"
    m = "Midlands"
    so = "South"
    i = "Ireland"
    REGIONCHOICES = (
        (s, "Scotland"),
        (n, "North"),
        (m, "Midlands"),
        (so, "South"),
        (i, "Ireland"),
    )
    region = models.CharField(max_length=10, 
        choices=REGIONCHOICES, default="Midlands")
    size = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    money = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)

    def __str__(self):
        return self.name