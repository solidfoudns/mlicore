
from django.conf.urls import url
from django.contrib import admin
from ventas import views
urlpatterns = [

    url(r'^carrito/$', views.carrito, name='carrito'),
    url(r'^calendario/$', views.calendario_eventos, name='calendario'),



]