# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    next_page = request.GET['next']
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        return render(request, next_page + 'login', {'login_error': True})

def user_logout(request):
    logout(request)
    return redirect(request.GET.get('next', None))
