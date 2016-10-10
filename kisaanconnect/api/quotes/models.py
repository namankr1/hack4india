from __future__ import unicode_literals
from userprofile.models import Profile
from categorization.models import Subcategory
from django.db import models

# Create your models here.

class Quote(models.Model):
    profile = models.ForeignKey(Profile)
    subcategory = models.ForeignKey(Subcategory)
    type = models.CharField(max_length=70)
    quantity = models.FloatField()
    price = models.FloatField()
    description = models.TextField(null=True,default=None)
    bidvalue = models.FloatField(null=True,default=None)
    is_active = models.BooleanField(default=True) 

class Rating(models.Model):
    profile = models.ForeignKey(Profile)
    subcategory = models.ForeignKey(Subcategory)
    rating  = models.IntegerField()