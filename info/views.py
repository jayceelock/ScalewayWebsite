# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'info/home.html', {})

def portfolio(request):
    return render(request, 'info/portfolio.html', {})

def publications(request):
    return render(request, 'info/publications.html', {})

def cv(request):
    return render(request, 'info/cv.html', {})

def blog(request):
    return render(request, 'info/blog.html', {})

def about(request):
    return render(request, 'info/about.html', {})

def contact(request):
    return render(request, 'info/.html', {})
