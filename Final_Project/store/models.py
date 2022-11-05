from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50, unique = True)
    description = models.TextField(max_length = 200, unique=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products', blank = True)
    category = models.ForeignKey(Category, on_delete =  models.CASCADE)
    slug = models.CharField(max_length = 200, unique = True)

    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug])

    def __str__(self):
        return self.product_name