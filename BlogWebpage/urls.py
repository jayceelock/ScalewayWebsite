from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^', views.blog_posts, name="blog_posts"),
        ]
