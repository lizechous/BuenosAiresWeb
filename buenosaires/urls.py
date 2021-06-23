"""buenosaires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.BuenosAires.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register', TemplateView.as_view(template_name='register.html'), name='register'),
    path('shop', TemplateView.as_view(template_name='shop.html'), name='shop'),
    path('shopping-cart', TemplateView.as_view(template_name='shopping-cart.html'), name='shopping-cart'),
    path('check-out', TemplateView.as_view(template_name='check-out.html'), name='check-out'),
    path('servicio', TemplateView.as_view(template_name='servicio.html'), name='servicio'),
]

