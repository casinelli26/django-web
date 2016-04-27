from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import SalesPerson, SalesAccounts
from .forms import SalesPersonForm, SalesAccountsForm
from django.http import HttpResponse

# Create your views here.
@login_required
def Sales(request):
	form = SalesPersonForm(request.POST or None)
	if form.is_valid():
		new_salesperson = form.save(commit=True)
		return HttpResponseRedirect('/sales')
	salesperson_info = SalesPerson.objects.order_by('date_added')
	context = {'form':form, 'salesperson_info':salesperson_info}
	template = 'sales.html'
	return render(request, template, context)

# @login_required
# def SalesInfo(request,id):
# 	form = SalesAccountsForm(request.POST or None)
# 	if form.is_valid():
# 		new_account = form.save(commit=True)
# 		return HttpResponseRedirect('/sales/' + id)
# 	salesaccount_info = SalesAccounts.objects.order_by('updated')
# 	salesperson_info = SalesPerson.objects.order_by('date_added')
# 	context = {'form':form, 'salesaccount_info':salesaccount_info, 'salesperson_info':salesperson_info}
# 	template = 'salesinfo.html'
# 	return render(request,template,context)

def SalesDetail(request,id):
	form = SalesAccountsForm(request.POST or None)
	if form.is_valid():
		new_account = form.save(commit=True)
		return HttpResponseRedirect('/sales/' + id)
	salesaccount_info = SalesAccounts.objects.all().filter(id=id)
	context = {'form':form, 'salesaccount_info':salesaccount_info}
	template = 'salesinfo.html'
	return render(request,template,context)
