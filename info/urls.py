from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^projects/', views.projects, name="projects"),
        url(r'^publications/', views.publications, name="publications"),
        url(r'^', views.home, name="home"),
        ]
