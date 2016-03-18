__author__ = 'mrk2'

from django.conf.urls import url
from django.contrib import admin
from inventatio import views
urlpatterns = [

    url(r'^inventario/$', views.inventario, name='inventario'),
    url(r'^articulo/$', views.articulo, name='artuculo'),
    url(r'^categorias/$', views.categorias, name='categorias'),
    url(r'^categoria/$', views.categoria, name='categoria'),
    url(r'^proveedores/$', views.provedores, name='provedores'),
    url(r'^proveedor/$', views.provedor, name='provedor'),


]
