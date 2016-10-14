from __future__ import unicode_literals

from django.db import models
from userprofile.models import Profile
from quotes.models import Quote

# Create your models here.
class GovtNotification(models.Model):
	title = models.TextField()
	body = models.TextField()
	url = models.CharField(max_length=150)

class AccountNotification(models.Model):
	sender = models.ForeignKey(Profile, related_name = 'nofication_sender')
	reciever = models.ForeignKey(Profile, related_name = 'notification_reciever')
	quote = models.ForeignKey(Quote)
	price = models.FloatField()
	quantity = models.FloatField()
	status = models.IntegerField()
	