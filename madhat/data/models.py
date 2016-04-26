from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SalesPerson(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20, default=None)
	id = models.AutoField(primary_key=True)
	date_added = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	def __unicode__(self):
		return self.first_name

	def get_full_name(self):
		return ' '.join(self.first_name, self.last_name)
	
	class Meta:
		unique_together = ('first_name', 'last_name')


class SalesAccounts(models.Model):
	account_name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add= True, auto_now=False)
	updated = models.DateTimeField(auto_now_add= False, auto_now=True)
	lead_sales_person = models.ForeignKey(SalesPerson)