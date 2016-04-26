from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from madhat import settings
import os
from django import template

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def Welcome(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            messages.error(request, 'INVALID USERNAME')
            return HttpResponseRedirect(settings.LOGIN_URL)
    context = {'redirect_to':next}
    template = 'welcome.html'
    return render(request, template, context)

def Test(request):
    context = {}
    template = 'test.html'
    return render(reqeust, template, context)

def About(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)