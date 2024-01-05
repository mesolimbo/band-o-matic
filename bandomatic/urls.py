"""
URL configuration for bandomatic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView

import greet.views

urlpatterns = [
    path('gallery.html', TemplateView.as_view(template_name="gallery.html"), name='band_gallery'),
    path('privacy.html', greet.views.privacy, name='privacy'),
    path('api/v1/', include("restapi.urls"), name='api-docs'),
    # Uncomment this and the entry in `INSTALLED_APPS` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
    path('admin/', admin.site.urls, name='admin'),
    path('', greet.views.index, name='index'),
]
