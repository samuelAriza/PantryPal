from django.db import models

# Create your models here.
class PublishProduct(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='products/')
    product_type = models.CharField(max_length=30)
    quantity = models.IntegerField()
    publish_price = models.CharField(max_length=300)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)

    def __str__(self):
        return self.name