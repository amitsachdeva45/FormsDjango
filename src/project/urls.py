"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from project import views
from forms.views import forms, normalForm, modelForm, testFormSet, modelFormSet, modelFormSetQuerySet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^form/$', forms, name='forms'),
    url(r'^normalForm/$', normalForm, name='normalForm'),
    url(r'^modelForm/$', modelForm, name='modelForm'),
    url(r'testFormSet/$', testFormSet, name='testFormSet'),
    url(r'modelFormSet/$', modelFormSet, name='modelFormSet'),
    url(r'modelFormSetQuerySet/$', modelFormSetQuerySet, name='modelFormSetQuerySet'),
]
