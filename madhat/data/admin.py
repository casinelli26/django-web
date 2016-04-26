from django.contrib import admin
from .models import SalesPerson, SalesAccounts

# Register your models here.
class SalesPersonAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'id']
	class Meta:
		model = SalesPerson

class SalesAccountsAdmin(admin.ModelAdmin):
	list_display = ['account_name', 'lead_sales_person']
	class Meta:
		model = SalesAccounts

admin.site.register(SalesPerson, SalesPersonAdmin)
admin.site.register(SalesAccounts, SalesAccountsAdmin)