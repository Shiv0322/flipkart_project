from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    Id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Order {self.Id} for {self.product.name}"