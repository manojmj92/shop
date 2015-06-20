"""shopify URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shopify_app.views.login', name = 'login'),
    url(r'^home/', 'shopify_app.views.home', name = 'home'),
    url(r'^set/', 'shopify_app.views.save_store_details', name = 'save_store_details'),
    url(r'^logout/', 'shopify_app.views.logout', name = 'logout'),
    url(r'^search/', 'shopify_app.views.search', name = 'search'),
    url(r'^reload/', 'shopify_app.views.reload', name = 'reload'),

]