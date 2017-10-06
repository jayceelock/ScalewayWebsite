# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.core.urlresolvers import resolve

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    next_page = request.GET['next']
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        return redirect(next_page)# return resolve(next_page)[0]
        # return render(request, resolve(next_page)[0], {'login_error': True})

def user_logout(request):
    logout(request)
    return redirect(request.GET.get('next', None))
