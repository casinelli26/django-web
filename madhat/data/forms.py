from django import forms
from .models import SalesPerson, SalesAccounts

class SalesPersonForm(forms.ModelForm):
	class Meta:
		model = SalesPerson
		fields = ['first_name', 'last_name']

class SalesAccountsForm(forms.ModelForm):
	class Meta:
		model = SalesAccounts
		fields = ['account_name', 'lead_sales_person', 'id']