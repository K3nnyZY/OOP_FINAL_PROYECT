from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50, unique = True)
    description = models.TextField(max_length = 200, unique=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products', blank = True)
    category = models.ForeignKey(Category, on_delete =  models.CASCADE)

    def __str__(self):
        return self.product_name