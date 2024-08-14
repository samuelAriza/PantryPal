from django.db import models

# Create your models here.
class sale_products(models.Model):
    product_id = models.IntegerField()
    product_type = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.CharField(max_length=30)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    