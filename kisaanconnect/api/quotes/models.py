from __future__ import unicode_literals
from userprofile.models import Profile
from categorization.models import Subcategory
from django.db import models

# Create your models here.

class Quote(models.Model):
    #Profile to which the quote belongs to
    profile = models.ForeignKey(Profile)
    #Subcategory to which the quote belongs to
    subcategory = models.ForeignKey(Subcategory)
    #Type of the quote
    type = models.TextField()
    #Quantity of the item to be added to quote
    quantity = models.FloatField()
    #Price of the quote
    price = models.FloatField()
    #Optional description to be included in the quote
    description = models.TextField(null=True,default=None)
    #Current bid value of the quotation
    bidvalue = models.FloatField(null=True,default=None)
    #Active or disable feature
    is_active = models.BooleanField(default=True)

class Rating(models.Model):
    profile = models.ForeignKey(Profile)
    subcategory = models.ForeignKey(Subcategory)
    rating  = models.IntegerField()
