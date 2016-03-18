__author__ = 'mrk2'

from django.conf.urls import url
from django.contrib import admin
from reportes import views
urlpatterns = [

    url(r'^$', views.index, name='index'),

]
