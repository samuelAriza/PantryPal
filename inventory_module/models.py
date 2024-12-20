from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    sale_price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='inventory/image/')
    pick_up_address = models.CharField(max_length=200,null=True)
    place = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    def image_url(self):
        return self.image.url
class Inventory(models.Model):
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['creation_date'], name='unique_creation_date')
        ]
    def __str__(self):
        return f'Inventory ({self.creation_date})'
    
class Product_Inventory(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    total_quantity = models.IntegerField()
    class Meta:
        unique_together = ('id_product', 'id_inventory')
    @property
    def name_product(self):
        return self.id_product.name
    @property
    def category_product(self):
        return self.id_product.category
    @property
    def sale_price_product(self):
        return self.id_product.sale_price
    @property
    def description_product(self):
        return self.id_product.description
    @property
    def image_product(self):
        return self.id_product.image_url
    @property
    def pick_up_address(self):
        return self.id_product.pick_up_address
class Published_Product(models.Model):
    id_product_inventory = models.ForeignKey(Product_Inventory, on_delete=models.CASCADE)
    publish_type = models.CharField(max_length=20)
    publish_quantity = models.PositiveIntegerField()
    publish_price = models.PositiveIntegerField()
    pick_up_time = models.TimeField()
    
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    @property
    def name_product(self):
        return self.id_product_inventory.name_product
    
    @property
    def category_product(self):
        return self.id_product_inventory.category_product
    
    @property
    def description_product(self):
        return self.id_product_inventory.description_product
    @property
    def image_product(self):
        return self.id_product_inventory.image_product
    @property
    def pick_up_address(self):
        return self.id_product_inventory.id_product.pick_up_address
    @property
    def place(self):
        return self.id_product_inventory.id_product.place

class Wasted_Product(models.Model):
    id_product_inventory = models.ForeignKey(Product_Inventory, on_delete=models.CASCADE)
    wasted_quantity = models.PositiveIntegerField()  
    wasted_date = models.DateField(auto_now_add=True)  

    def __str__(self):
        return f"{self.id_product_inventory.name_product} - {self.wasted_quantity} desperdiciados"
    
    @property
    def name_product(self):
        return self.id_product_inventory.name_product
    
    @property
    def category_product(self):
        return self.id_product_inventory.category_product
    
    @property
    def description_product(self):
        return self.id_product_inventory.description_product

    @property
    def image_product(self):
        return self.id_product_inventory.image_product

    @property
    def pick_up_address(self):
        return self.id_product_inventory.pick_up_address

    @property
    def place(self):
        return self.id_product_inventory.place


