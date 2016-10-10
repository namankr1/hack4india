#External libraries
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountType = models.CharField(max_length=1) # I,C
    picture = models.ImageField(upload_to='profilepictures', default='profilepictures/default.jpg');
    location = models.ForeignKey(Location,null=True)

class OTPRecord(models.Model):
    otp = models.CharField(max_length=6)
    profile = models.ForeignKey(Profile)


