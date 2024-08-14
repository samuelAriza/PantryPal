from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20) 
    total_quantity = models.IntegerField()
    sale_price = models.IntegerField()
    def __str__(self):
        return self.name
