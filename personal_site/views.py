# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    print "login"
    return HttpResponse("Hello")
