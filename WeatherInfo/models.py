from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CityWeather(models.Model):
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=10)
	date = models.DateField(auto_now_add=False)
	tem = models.IntegerField()
	wind = models.CharField(max_length=100)
	cloud = models.CharField(max_length=20)
	schema = models.CharField(max_length=100)
	tips=models.CharField(max_length=200)
	date2 = models.DateField(blank=True,auto_now_add=False)
	tem2 = models.IntegerField(blank=True,)
	wind2 = models.CharField(blank=True,max_length=100)
	date3 = models.DateField(blank=True,auto_now_add=False)
	tem3 = models.IntegerField(blank=True,)
	wind3 = models.CharField(blank=True,max_length=100)
	introduction = models.CharField(blank=True,max_length=500)

	def __unicode__(self):
		return self.name





