from django.db import models
from datetime import datetime
from django.utils.timezone import timezone

from django.contrib.auth.models import User

# Create your models here.

class Trade(models.Model):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User , on_delete=models.DO_NOTHING, blank=True)
	trading_ammount = models.IntegerField()
	profit = models.IntegerField()
	intrestrate = models.IntegerField()
	is_published = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now , blank=True)


	def __str__(self):
		return self.title;
