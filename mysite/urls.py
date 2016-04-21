"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^search_results/$', views.search_results),
    url(r'^kaplan/$', views.kaplan),
    url(r'^make_kaplan/$', views.make_kaplan),
    url(r'^download_kaplan/$', views.download_kaplan),
    url(r'^all_genes/$', views.gene_list),
    url(r'^all_ids/$', views.id_list),
    url(r'^cancer/$', views.cancer),
    url(r'^download_excel/$', views.download_excel),
    url(r'^plot_error/$', views.plot_error),
    url(r'^download/$', views.download)
]
