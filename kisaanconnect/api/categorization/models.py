from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='categorypictures', default='categorypictures/default.jpg');

class Subcategory(models.Model):
    name = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='subcategorypictures', default='subcategorypictures/default.jpg');
    category = models.ForeignKey(Category)
    