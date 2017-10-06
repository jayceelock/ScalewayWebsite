# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request, login_error=False):
    return render(request, 'info/home.html', {})

def projects(request, login_error=False):
    return render(request, 'info/projects.html', {})

def publications(request, login_error=False):
    return render(request, 'info/publications.html', {})
