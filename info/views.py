# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'info/home.html', {'title': 'Jacobus Lock - Engineer',
        'description': "Jacobus Lock's homepage"})

def portfolio(request):
    return render(request, 'info/portfolio.html', {'title': 'Jacobus Lock - Project Portfolio',
        'description': "Jacobus Lock's project portfolio"})

def publications(request):
    return render(request, 'info/publications.html', {'title': 'Jacobus Lock - Publications',
        'description': "Jacobus Lock's list of publications"})

def cv(request):
    return render(request, 'info/cv.html', {'title': 'Jacobus Lock - CV',
        'description': "Jacobus Lock's CV"})

def blog(request):
    return render(request, 'info/blog.html', {'title': 'Jacobus Lock - Blog',
        'description': "Jacobus Lock's small blog"})

def about(request):
    return render(request, 'info/about.html', {'title': 'Jacobus Lock - About Me',
        'description': "About Jacobus Lock"})

def contact(request):
    return render(request, 'info/.html', {})
