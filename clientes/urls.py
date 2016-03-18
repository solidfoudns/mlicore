__author__ = 'mrk2'

from django.conf.urls import url

from clientes import views
urlpatterns = [

    url(r'^clientes/$', views.clientes, name='clientess'),
    url(r'^cliente/$', views.cliente, name='cliente'),



]
