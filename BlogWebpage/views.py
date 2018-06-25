# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse

from models import Blog, Category

def blog_posts(request):
    return render_to_response('BlogWebpage/blog_posts.html',
            {
                'categories': Category.objects.all(),
                'posts': Blog.objects.all(), 
            })
