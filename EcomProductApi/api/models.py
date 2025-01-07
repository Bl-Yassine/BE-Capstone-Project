from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} ({self.id})"


#Product Model
class Product(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=255 ,blank=False)
    price = models.FloatField(blank=False)
    stock_quantity = models.IntegerField(blank=False)
    Image_URL = models.URLField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name


#Order Model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name



