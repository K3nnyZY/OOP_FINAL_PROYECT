from enum import unique
from pyexpat import model
from re import T
from statistics import mode
from tokenize import blank_re
from typing import Tuple
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 20, unique = True)
    description = models.CharField(max_length = 255, blank = True)
    slug = models.CharField(max_length = 100, unique =  True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name