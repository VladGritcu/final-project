from django.db import models
from django.db.models import Model, CharField, ForeignKey, IntegerField, DateField, TextField, DecimalField
# Create your models here.

    
class Brand(models.Model):
    name = models.CharField(max_length=128)
    # logo = models.ImageField(upload_to="brands/",blank=True)

        

    def __str__(self):
        return f"{self.name}"
    
class Tshirt(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    released = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    stock = models.PositiveIntegerField(max_length=32)
    size = models.CharField(max_length=5, choices=[('S','S'),('M','M'),('L','L'),('XL','XL')])
    color = models.CharField(max_length=32)
    # image = models.ImageField(uploade_to="tshirt/", blank=True)

    def __str__(self):
        return f"{self.name}"