from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    size = models.CharField(max_length=30, null=False, blank=False)
    friendliness = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, null=False, blank=False)
    color = models.CharField(max_length=20)
    favoritefood = models.CharField(max_length=20)
    favoritetoy = models.CharField(max_length=20)

    def __str__(self):
        return self.name
