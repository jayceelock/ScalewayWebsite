# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'BaseWebpage/home.html', {})

def projects(request):
    return render(request, 'BaseWebpage/projects.html', {})

def publications(request):
    return render(request, 'BaseWebpage/publications.html', {})
