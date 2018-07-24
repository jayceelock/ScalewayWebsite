from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^portfolio/', views.portfolio, name="portfolio"),
        url(r'^publications/', views.publications, name="publications"),
        url(r'^cv/', views.cv, name="cv"),
        url(r'^blog/', views.blog, name="blog"),
        url(r'^about/', views.about, name="about"),
        url(r'^contact/', views.contact, name="contact"),
        url(r'^', views.home, name="home"),
        ]
